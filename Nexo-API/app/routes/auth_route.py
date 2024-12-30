from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import AuthController

class AuthRoutes:
    def __init__(self):
        self.auth_controller = AuthController()
        self.auth_bp = Blueprint('auth', __name__)
        self._register_routes()

    def _register_routes(self):
        self.auth_bp.route('/register', methods=['POST'])(self.register)
        self.auth_bp.route('/login', methods=['POST'])(self.login)

    def register(self):
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Formato JSON inválido'}), 400
        
        cpf_cnpj = data.get('cpf_cnpj')
        password = data.get('password')
        
        if not cpf_cnpj or not password:
            return jsonify({'message': 'CPF/CNPJ e senha são obrigatórios'}), 400

        return self.auth_controller.register_user(cpf_cnpj, password)

    def login(self):
        data = request.get_json()
        if data is None:
            return jsonify({'message': 'Formato JSON inválido'}), 400
        
        cpf_cnpj = data.get('cpf_cnpj')
        password = data.get('password')
        
        if not cpf_cnpj or not password:
            return jsonify({'message': 'CPF/CNPJ e senha são obrigatórios'}), 400

        return self.auth_controller.authenticate_user(cpf_cnpj, password)

    def get_blueprint(self):
        return self.auth_bp
    