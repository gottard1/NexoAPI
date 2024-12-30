from validate_docbr import CPF, CNPJ
from flask import jsonify, current_app
from app.models.user_model import User
from app import db
import jwt

class AuthController:
    def __init__(self):
        self.cpf_validator = CPF()
        self.cnpj_validator = CNPJ()

    def register_user(self, cpf_cnpj, password):
        if not self._is_valid_cpf_cnpj(cpf_cnpj):
            return jsonify({'message': 'CPF ou CNPJ inválido'}), 400
        
        if User.query.filter_by(cpf_cnpj=cpf_cnpj).first():
            return jsonify({'message': 'Usuário já cadastrado'}), 400
        
        new_user = User(cpf_cnpj=cpf_cnpj)
        new_user.set_password(password)
        
        # Verifique se o password_hash foi gerado corretamente
        print(f"Password hash: {new_user.password_hash}")
        
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'Usuário cadastrado com sucesso'}), 200

    def authenticate_user(self, cpf_cnpj, password):
        user = User.query.filter_by(cpf_cnpj=cpf_cnpj).first()
        
        if user and user.check_password(password):
            token = jwt.encode({'user_id': user.id}, current_app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'token': token}), 200
        
        return jsonify({'message': 'Credenciais inválidas'}), 400
    
    """
    Verifica se o CPF ou CNPJ é válido.
    """
    def _is_valid_cpf_cnpj(self, cpf_cnpj):
        return self.cpf_validator.validate(cpf_cnpj) or self.cnpj_validator.validate(cpf_cnpj)