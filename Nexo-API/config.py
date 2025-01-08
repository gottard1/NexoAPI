import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///dev.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    DEBUG = True

class TestingConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///test.db')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    TESTING = True
    DEBUG = True

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgres://user:password@localhost/dbname')  # Banco de dados para produção

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    # 'production': ProductionConfig
}