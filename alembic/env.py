import os
import sys
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv

# 1. Garante que o Python encontre a pasta 'src'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# 2. Importa o seu Base e os Modelos (TB-012)
from src.database.models import Base
from src.database import models # Garante que todos os modelos sejam carregados

# 3. Carrega as variáveis do .env
load_dotenv()

config = context.config

# 4. Configura o logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 5. Define o metadata para o autogenerate
target_metadata = Base.metadata

def run_migrations_online() -> None:
    # 6. Usa a URL do seu .env dinamicamente
    url = os.getenv("DATABASE_URL")
    
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
        url=url,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    # Simplificado para o modo online que usaremos
    pass
else:
    run_migrations_online()