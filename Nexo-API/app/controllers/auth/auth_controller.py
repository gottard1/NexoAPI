from validate_docbr import CPF, CNPJ
from flask import current_app
from app.models.auth.user_model import User
from app.utils.validators import is_valid_cpf_cnpj, is_valid_email, is_valid_password
from app.models.auth.register_response import RegisterResponse
from app.models.generic_failure import GenericFailure
from app import db
import jwt

class AuthController:
    def __init__(self):
        self.cpf_validator = CPF()
        self.cnpj_validator = CNPJ()

    def register_user(self, cpf_cnpj, email, password):
        if not is_valid_cpf_cnpj(cpf_cnpj):
            return GenericFailure('CPF/CNPJ inválido').to_json(), 400

        if User.query.filter_by(cpf_cnpj=cpf_cnpj).first():
            return GenericFailure('CPF/CNPJ já cadastrado').to_json(), 400

        if not is_valid_email(email):
            return GenericFailure('E-mail inválido').to_json(), 400

        if User.query.filter_by(email=email).first():
            return GenericFailure('E-mail já cadastrado').to_json(), 400

        if not is_valid_password(password):
            return GenericFailure(
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
            failure = GenericFailure(f'Erro interno: {str(e)}')
            return failure.to_json(), 500

    def authenticate_user(self, cpf_cnpj, password):
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

        return GenericFailure('Credenciais inválidas').to_json(), 400

    def validate_code(self, code):
        if not code or len(code) != 6 or not code.isdigit():
            failure = GenericFailure('Código inválido')
            return failure.to_json(), 400
        return '', 204