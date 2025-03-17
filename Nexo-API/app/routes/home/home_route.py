from flask import Blueprint, request, jsonify
from app.controllers.home.home_controller import HomeController
from app.models.generic_failure import GenericFailure
from app.utils.validators import is_valid_cpf_cnpj

class HomeRoutes:
    def __init__(self):
        self.home_controller = HomeController()
        self.home_bp = Blueprint('home', __name__)
        self._register_routes()

    def _register_routes(self):
        """Registra as rotas no blueprint."""
        self.home_bp.route('/components', methods=['GET'])(self.get_components)
        self.home_bp.route('/components', methods=['POST'])(self.save_components)

    def get_components(self):
        cpf_cnpj = request.args.get('cpf_cnpj')
        if not cpf_cnpj:
            failure = GenericFailure('CPF/CNPJ é obrigatório')
            return failure.to_json(), 400

        return self.home_controller.get_components(cpf_cnpj)

    def save_components(self):
        data = request.get_json()
        if data is None:
            failure = GenericFailure('Formato JSON inválido')
            return failure.to_json(), 400

        cpf_cnpj = data.get('cpf_cnpj')
        components_json = data.get('components_json')

        if not cpf_cnpj or components_json is None:
            failure = GenericFailure('CPF/CNPJ e os componentes são obrigatórios')
            return failure.to_json(), 400

        return self.home_controller.save_components(cpf_cnpj, components_json)

    def get_blueprint(self):
        return self.home_bp