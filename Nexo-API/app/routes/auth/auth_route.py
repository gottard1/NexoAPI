from flask import Blueprint, request
from app.controllers.auth.auth_controller import AuthController
from app.models.generic_failure import GenericFailure

class AuthRoutes:
    def __init__(self):
        self.auth_controller = AuthController()
        self.auth_bp = Blueprint('auth', __name__)
        self._register_routes()

    def _register_routes(self):
        self.auth_bp.route('/register', methods=['POST'])(self.register)
        self.auth_bp.route('/login', methods=['POST'])(self.login)
        self.auth_bp.route('/email/validateCode', methods=['POST'])(self.validate_code)

    def register(self):
        data = request.get_json()
        if data is None:
            failure = GenericFailure('Formato JSON inválido')
            return failure.to_json(), 400

        cpf_cnpj = data.get('cpf_cnpj')
        email = data.get('email')
        password = data.get('password')

        if not cpf_cnpj or not email or not password:
            failure = GenericFailure('CPF/CNPJ, e-mail e senha são obrigatórios')
            return failure.to_json(), 400

        return self.auth_controller.register_user(cpf_cnpj, email, password)

    def login(self):
        data = request.get_json()
        if data is None:
            failure = GenericFailure('Formato JSON inválido')
            return failure.to_json(), 400

        cpf_cnpj = data.get('cpf_cnpj')
        password = data.get('password')
        
        if not cpf_cnpj or not password:
            failure = GenericFailure('CPF/CNPJ e senha são obrigatórios')
            return failure.to_json(), 400

        return self.auth_controller.authenticate_user(cpf_cnpj, password)

    def get_blueprint(self):
        return self.auth_bp

    def validate_code(self):
        data = request.get_json()
        if data is None:
            failure = GenericFailure('Formato JSON inválido')
            return failure.to_json(), 400

        code = data.get('code')
        
        if not code:
            failure = GenericFailure('Código é obrigatório')
            return failure.to_json(), 400

        return self.auth_controller.validate_code(code)