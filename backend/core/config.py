import os
from pathlib import Path
from dotenv import load_dotenv
from jose.constants import ALGORITHMS

env_path = Path('.') / '.env'
#if not installed globally - install globally first then in venv
load_dotenv(dotenv_path=env_path)


class Settings:

    # Docs Information
    PROJECT_TITLE : str = "Jobboard"
    PROJECT_VERSION : str = "0.1.1"

    # Database information
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD : str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB : str = os.getenv("POSTGRES_DB", "db_course")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    #Authorization Information
    SECRET_KEY : str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30

    TEST_USER_EMAIL = "test@example.com"

settings = Settings()