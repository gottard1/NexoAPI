from flask import Flask
from config import Config
from app.db import db
from app.routes.auth_route import AuthRoutes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes.auth_route import AuthRoutes
    auth_routes = AuthRoutes()
    app.register_blueprint(auth_routes.get_blueprint(), url_prefix='/auth')

    with app.app_context():
        db.create_all()

    return app