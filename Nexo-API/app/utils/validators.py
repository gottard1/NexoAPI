import re
from validate_docbr import CPF, CNPJ

cpf_validator = CPF()
cnpj_validator = CNPJ()

def is_valid_cpf_cnpj(cpf_cnpj):
    return cpf_validator.validate(cpf_cnpj) or cnpj_validator.validate(cpf_cnpj)

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def is_valid_password(password):
    password_regex = r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return re.match(password_regex, password) is not None