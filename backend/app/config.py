import os


class Settings:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    HOST = '0.0.0.0'
    PORT = 8000
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///./db.sqlite3')


settings = Settings()