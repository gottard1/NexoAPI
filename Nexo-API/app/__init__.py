from flask import Flask
from config import Config
from app.db import db
from app.routes.auth.auth_route import AuthRoutes
from app.routes.home.home_route import HomeRoutes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.get_blueprint(), url_prefix='/auth')
    
    home_routes = HomeRoutes()
    app.register_blueprint(home_routes.get_blueprint(), url_prefix='/home')

    with app.app_context():
        db.create_all()

    return app