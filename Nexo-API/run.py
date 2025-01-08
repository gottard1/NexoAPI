import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.routes.auth_route import AuthRoutes
from config import app_config

db = SQLAlchemy()

def create_app(config_name='development'):
    app = Flask(__name__)
    
    app.config.from_object(app_config.get(config_name, app_config['development']))

    db.init_app(app)

    # Rotas para autenticação
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.get_blueprint(), url_prefix='/auth')

    return app

def run():
    config_name = os.getenv('FLASK_ENV', 'development')
    app = create_app(config_name)
    app.run(host='127.0.0.1', port=5000)

if __name__ == '__main__':
    run()