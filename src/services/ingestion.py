import pandas as pd
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database.models import Student, ImportBatch
from dotenv import load_dotenv

load_dotenv()

class DataIngestionService:
    def __init__(self):
        """Inicializa a conexão com o banco de dados."""
        self.engine = create_engine(os.getenv("DATABASE_URL"))
        self.Session = sessionmaker(bind=self.engine)

    def process_students_csv(self, file, filename: str):
        """Processa o upload de alunos e registra o lote com tratamento de erros."""
        # 1. Leitura e Limpeza Inicial (TB-016)
        df = pd.read_csv(file)
        # Remove espaços em branco dos nomes das colunas
        df.columns = [col.strip() for col in df.columns]
        # Trata valores vazios como 0.0 imediatamente
        df = df.fillna(0)
        
        # 2. Validação de Schema
        required_cols = ['name', 'segment', 'grade', 'full_tuition']
        for col in required_cols:
            if col not in df.columns:
                raise ValueError(f"Coluna obrigatória ausente: {col}")

        session = self.Session()
        try:
            # 3. Registro do Lote de Importação (Auditoria)
            # Nota Pro: Se receber erro de 'invalid keyword', 
            # confirme se no models.py está 'row_count' ou 'rows_imported'
            batch = ImportBatch(
                filename=filename,
                row_count=len(df),
                status="Success"
            )
            session.add(batch)
            session.flush() # Gera o ID do lote antes do commit final

            # 4. Ingestão Idempotente dos Alunos
            for _, row in df.iterrows():
                # Normalização para comparação (evita duplicados por espaço ou caixa)
                name_clean = str(row['name']).strip()
                grade_clean = str(row['grade']).strip()

                student_exists = session.query(Student).filter_by(
                    name=name_clean,
                    grade=grade_clean
                ).first()

                if not student_exists:
                    new_student = Student(
                        name=name_clean,
                        segment=str(row['segment']).strip(),
                        grade=grade_clean,
                        classroom=str(row.get('classroom', 'A')).strip(),
                        status='Ativo',
                        full_tuition=float(row['full_tuition']),
                        discount_value=float(row.get('discount_value', 0)),
                        scholarship_value=float(row.get('scholarship_value', 0)),
                        batch_id=batch.id
                    )
                    session.add(new_student)
            
            session.commit()
            return f"✅ Lote #{batch.id} processado: {len(df)} linhas lidas."

        except Exception as e:
            session.rollback()
            # Log técnico no terminal para facilitar o seu debug
            print(f"DEBUG [Ingestion]: Falha ao processar {filename}. Detalhe: {e}")
            raise e
        finally:
            session.close()