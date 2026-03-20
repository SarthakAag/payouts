import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SECRET_KEY = os.getenv("SECRET_KEY", "3d6f45a5fc12445dbac2f59a3e15b8e6a58b9c3d0e4f1a2b7c8d9e0f1a2a45v")
    DEBUG = os.getenv("DEBUG") == "True"
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))
    DATABASE_URL=os.getenv("DATABASE_URL")
    

settings = Settings()