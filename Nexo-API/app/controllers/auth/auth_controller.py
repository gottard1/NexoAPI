from validate_docbr import CPF, CNPJ
from flask import jsonify, current_app
from app.models.auth.user_model import User
from app.utils.validators import is_valid_cpf_cnpj, is_valid_email, is_valid_password
from app.models.auth.Register.register_response import RegisterResponse
from app.models.auth.Register.register_failure import RegisterFailure
from app import db
import jwt

class AuthController:
    def __init__(self):
        self.cpf_validator = CPF()
        self.cnpj_validator = CNPJ()

    def register_user(self, cpf_cnpj, email, password):
        if not is_valid_cpf_cnpj(cpf_cnpj):
            return RegisterFailure('CPF/CNPJ inválido').to_json(), 400

        if User.query.filter_by(cpf_cnpj=cpf_cnpj).first():
            return RegisterFailure('CPF/CNPJ já cadastrado').to_json(), 400

        if not is_valid_email(email):
            return RegisterFailure('E-mail inválido').to_json(), 400

        if User.query.filter_by(email=email).first():
            return RegisterFailure('E-mail já cadastrado').to_json(), 400

        if not is_valid_password(password):
            return RegisterFailure(
                'Senha inválida. A senha deve ter ao menos 8 caracteres, incluir uma letra maiúscula, '
                'um número e um caractere especial.'
            ).to_json(), 400

        try:
            new_user = User(cpf_cnpj=cpf_cnpj, email=email)
            new_user.set_password(password)

            db.session.add(new_user)
            db.session.commit()

            token = jwt.encode(
                {'user_id': new_user.id},
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            return RegisterResponse(
                message='Usuário cadastrado com sucesso',
                token=token
            ).to_json(), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'message': f'Erro interno: {str(e)}'}), 500

    def authenticate_user(self, cpf_cnpj, password):
        """Autentica um usuário existente."""
        user = User.query.filter_by(cpf_cnpj=cpf_cnpj).first()

        if user and user.check_password(password):
            token = jwt.encode(
                {'user_id': user.id},
                current_app.config['SECRET_KEY'],
                algorithm='HS256'
            )
            return RegisterResponse(
                message='Usuário autenticado com sucesso',
                token=token
            ).to_json(), 200

        return RegisterFailure('Credenciais inválidas').to_json(), 400

    def validate_code(self, code):
        """Valida o código fornecido."""
        if not code or len(code) != 6 or not code.isdigit():
            return jsonify({'message': 'Código inválido'}), 400
        return '', 204