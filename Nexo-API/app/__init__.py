from flask import Flask
from config import DevelopmentConfig
from app.db import db
from app.routes.auth.auth_route import AuthRoutes

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)

    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.get_blueprint(), url_prefix='/auth')

    with app.app_context():
        db.create_all()

    return app