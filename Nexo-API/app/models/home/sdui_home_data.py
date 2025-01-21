from app import db
from flask import jsonify

class SDUIHomeDataModel(db.Model):
    __tablename__ = 'sdui_home_data'

    id = db.Column(db.Integer, primary_key=True)
    cpf_cnpj = db.Column(db.String(14), unique=True, nullable=False)
    components_json = db.Column(db.JSON, nullable=False)

    def __init__(self, cpf_cnpj, components_json):
        self.cpf_cnpj = cpf_cnpj
        self.components_json = components_json

    def to_json(self):
        return jsonify(self.__dict__)
    
    @classmethod
    def find_by_cpf_cnpj(cls, cpf_cnpj):
        return cls.query.filter_by(cpf_cnpj=cpf_cnpj).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, components_json):
        self.components_json = components_json
        db.session.commit()