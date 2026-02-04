import os

class Config:
    APP_NAME = os.getenv("APP_NAME", "Two-Tier Flask App")
    ENV = os.getenv("ENV", "development")

    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "root")
    DB_NAME = os.getenv("DB_NAME", "twotierdb")
    DB_PORT = int(os.getenv("DB_PORT", 3307))
