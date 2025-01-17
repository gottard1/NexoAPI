from flask import Blueprint, request, jsonify
from app.controllers.auth.auth_controller import AuthController

class AuthRoutes:
    """Define as rotas relacionadas à autenticação e registro."""
    def __init__(self):
        self.auth_controller = AuthController()
        self.auth_bp = Blueprint('auth', __name__)
        self._register_routes()

    def _register_routes(self):
        """Registra as rotas no blueprint."""
        self.auth_bp.route('/register', methods=['POST'])(self.register)
        self.auth_bp.route('/login', methods=['POST'])(self.login)
        self.auth_bp.route('/email/validateCode', methods=['POST'])(self.validate_code)

    def register(self):
        """Endpoint para registro de novos usuários."""
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Formato JSON inválido'}), 400

        cpf_cnpj = data.get('cpf_cnpj')
        email = data.get('email')
        password = data.get('password')

        if not cpf_cnpj or not email or not password:
            return jsonify({'message': 'CPF/CNPJ, e-mail e senha são obrigatórios'}), 400

        return self.auth_controller.register_user(cpf_cnpj, email, password)

    def login(self):
        """Endpoint para login de usuários."""
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Formato JSON inválido'}), 400

        cpf_cnpj = data.get('cpf_cnpj')
        password = data.get('password')

        if not cpf_cnpj or not password:
            return jsonify({'message': 'CPF/CNPJ e senha são obrigatórios'}), 400

        return self.auth_controller.authenticate_user(cpf_cnpj, password)

    def validate_code(self):
        """Endpoint para validação de códigos."""
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Formato JSON inválido'}), 400

        code = data.get('code')

        if not code:
            return jsonify({'message': 'Código é obrigatório'}), 400

        return self.auth_controller.validate_code(code)

    def get_blueprint(self):
        """Retorna o blueprint configurado."""
        return self.auth_bp