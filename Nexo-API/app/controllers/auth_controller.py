from validate_docbr import CPF, CNPJ
from flask import jsonify, current_app

from app.models.user_model import User
from app.utils.validators import is_valid_cpf_cnpj, is_valid_email, is_valid_password
from app.models.Register.register_response import RegisterResponse
from app.models.Register.register_failure import RegisterFailure

from app import db
import jwt

class AuthController:
    def __init__(self):
        self.cpf_validator = CPF()
        self.cnpj_validator = CNPJ()

    def register_user(self, cpf_cnpj, email, password):
        if not is_valid_cpf_cnpj(cpf_cnpj):
            response = RegisterFailure('CPF/CNPJ inválido')
            return response.to_json(), 400

        if User.query.filter_by(cpf_cnpj=cpf_cnpj).first():
            response = RegisterFailure('CPF/CNPJ já cadastrado')
            return response.to_json(), 400

        if not is_valid_email(email):
            response = RegisterFailure('E-mail inválido')
            return response.to_json(), 400

        if User.query.filter_by(email=email).first():
            response = RegisterFailure('E-mail já cadastrado')
            return response.to_json(), 400

        if not is_valid_password(password):
            response = RegisterFailure('Senha inválida. A senha deve ter ao menos 8 caracteres, incluir uma letra maiúscula, um número e um caractere especial.')
            return response.to_json(), 400

        new_user = User(cpf_cnpj=cpf_cnpj, email=email)
        new_user.set_password(password)

        db.session.add(new_user)
        db.session.commit()
        
        if new_user and new_user.check_password(password):
            token = jwt.encode({'user_id': new_user.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

            response = RegisterResponse(
                message = 'Usuário cadastrado com sucesso',
                token = token
            )
            return response.to_json(), 200

    def authenticate_user(self, cpf_cnpj, password):
        user = User.query.filter_by(cpf_cnpj=cpf_cnpj).first()

        if user and user.check_password(password):
            token = jwt.encode({'user_id': user.id}, current_app.config['SECRET_KEY'], algorithm='HS256')

            response = RegisterResponse(
                message = 'Usuário autenticado com sucesso',
                token = token
            )
            return response.to_json(), 200

        response = RegisterFailure('Credenciais inválidas')
        return response.to_json(), 400
    
    def validate_code(self, code):
        if not code or len(code) != 6 or not code.isdigit():
            return jsonify({'message': 'Código inválido'}), 400
    
        return '', 204