import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "minha_chave_secreta")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///app.db")
    DEBUG = True

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///test.db')
    TESTING = True
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}