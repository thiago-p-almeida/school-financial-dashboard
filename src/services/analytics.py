import os
import io
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
from datetime import datetime

# Carrega as variáveis de ambiente (.env)
load_dotenv()

class SchoolAnalytics:
    def __init__(self):
        """Inicializa a conexão com o banco de dados PostgreSQL."""
        db_url = os.getenv("DATABASE_URL")
        if not db_url:
            raise ValueError("DATABASE_URL não encontrada no arquivo .env")
        self.engine = create_engine(db_url)

    def get_active_students_df(self) -> pd.DataFrame:
        """Retorna um DataFrame com alunos ativos e calcula a mensalidade líquida."""
        query = "SELECT * FROM students WHERE status = 'Ativo'"
        df = pd.read_sql(query, self.engine)
        
        if not df.empty:
            # Cálculo: Valor Cheio - Descontos - Bolsas (TB-014)
            df['net_tuition'] = df['full_tuition'] - df['discount_value'] - df['scholarship_value']
        return df

    def get_financial_summary(self, month: int, year: int = 2024) -> pd.DataFrame:
        """Resumo financeiro de receitas (Pago vs Pendente) por mês/ano."""
        query = f"""
            SELECT status, SUM(amount) as total
            FROM financial_transactions
            WHERE type = 'Receita' AND category = 'Mensalidade'
              AND EXTRACT(MONTH FROM reference_date) = {month}
              AND EXTRACT(YEAR FROM reference_date) = {year}
            GROUP BY status
        """
        return pd.read_sql(query, self.engine)

    def get_revenue_by_segment(self) -> pd.DataFrame:
        """Agrupa a receita líquida esperada por segmento acadêmico."""
        df = self.get_active_students_df()
        if df.empty:
            return pd.DataFrame(columns=['Segmento', 'Receita_Esperada'])
        
        segment_df = df.groupby('segment')['net_tuition'].sum().reset_index()
        segment_df.columns = ['Segmento', 'Receita_Esperada']
        return segment_df.sort_values(by='Receita_Esperada', ascending=False)

    def get_churn_analysis(self) -> dict:
        """Calcula as métricas de evasão (Churn) e motivos de saída."""
        query = "SELECT * FROM students"
        df = pd.read_sql(query, self.engine)
        
        if df.empty:
            return {
                "churn_rate": 0, "total_ativos": 0, 
                "total_inativos": 0, "reasons_df": pd.DataFrame()
            }
        
        total_historico = len(df)
        ativos = len(df[df['status'] == 'Ativo'])
        inativos = len(df[df['status'] == 'Inativo'])
        
        churn_rate = (inativos / total_historico) * 100 if total_historico > 0 else 0
        
        reasons_df = df[df['status'] == 'Inativo']['exit_reason'].value_counts().reset_index()
        reasons_df.columns = ['Motivo', 'Quantidade']
        
        return {
            "churn_rate": churn_rate,
            "total_ativos": ativos,
            "total_inativos": inativos,
            "reasons_df": reasons_df
        }

    def get_financial_forecasting(self, months=6, delinquency_rate=0.05) -> pd.DataFrame:
        """
        Gera uma projeção financeira para os próximos meses (TB-026).
        delinquency_rate: Taxa estimada de inadimplência (ex: 0.05 para 5%)
        """
        # 1. Calculamos a Receita Mensal Atual Base (Alunos Ativos)
        df_active = self.get_active_students_df()
        
        if df_active.empty:
            return pd.DataFrame(columns=["Mês", "Receita Bruta", "Receita Projetada (Líquida)", "Risco de Inadimplência"])
            
        monthly_revenue = df_active['net_tuition'].sum()
        
        # 2. Criamos a projeção temporal
        current_date = datetime.now()
        forecast_data = []
        
        for i in range(1, months + 1):
            # Simula o mês seguinte usando pandas Offset para precisão de calendário
            target_date = current_date + pd.DateOffset(months=i)
            
            # Cálculo de Receita Projetada com redutor de inadimplência (Risco)
            expected_revenue = monthly_revenue * (1 - delinquency_rate)
            risk_value = monthly_revenue * delinquency_rate
            
            forecast_data.append({
                "Mês": target_date.strftime('%b/%Y'),
                "Receita Bruta": monthly_revenue,
                "Receita Projetada (Líquida)": expected_revenue,
                "Risco de Inadimplência": risk_value
            })
            
        return pd.DataFrame(forecast_data)

    def to_excel(self, df: pd.DataFrame) -> bytes:
        """Converte um DataFrame para Excel em memória para download (TB-011)."""
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Projecao_Financeira')
        return output.getvalue()

# Bloco de teste
if __name__ == "__main__":
    test = SchoolAnalytics()
    print("Teste Forecasting (3 meses):")
    print(test.get_financial_forecasting(months=3))