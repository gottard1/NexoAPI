from flask import jsonify
from app.models.home.sdui_home_data import SDUIHomeDataModel
from app.models.home.home_components import HomeComponents
from app.models.generic_failure import GenericFailure
from app.utils.validators import is_valid_cpf_cnpj
from app import db

class HomeController:
    def __init__(self):
        pass

    def get_components(self, cpf_cnpj):
        if not is_valid_cpf_cnpj(cpf_cnpj):
            failure = GenericFailure('CPF/CNPJ inválido')
            return failure.to_json(), 400

        home_data = SDUIHomeDataModel.find_by_cpf_cnpj(cpf_cnpj)
    
        if home_data:
            components = HomeComponents(home_data.components_json)
            return components.to_json(), 200

        failure = GenericFailure('Dados não encontrados para o CPF/CNPJ fornecido')
        return failure.to_json(), 400

    def save_components(self, cpf_cnpj, components_json: list):
        if not is_valid_cpf_cnpj(cpf_cnpj):
            failure = GenericFailure('CPF/CNPJ inválido')
            return failure.to_json(), 400

        if not isinstance(components_json, list):
            failure = GenericFailure('O formato dos componentes deve ser JSON')
            return failure.to_json(), 400

        try:
            existing_data = SDUIHomeDataModel.find_by_cpf_cnpj(cpf_cnpj)
            if existing_data:
                existing_data.update(components_json)
            else:
                new_data = SDUIHomeDataModel(cpf_cnpj=cpf_cnpj, components_json=components_json)
                db.session.add(new_data)
                db.session.commit()

            return jsonify({'message': 'Dados salvos com sucesso'}), 200
        except Exception as e:
            db.session.rollback()
            failure = GenericFailure(f'Erro interno: {str(e)}')
            return failure.to_json(), 500