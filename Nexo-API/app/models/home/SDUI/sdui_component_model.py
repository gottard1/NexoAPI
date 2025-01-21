from flask import jsonify
from app.models.home.SDUI.sdui_config_model import SDUIConfig
from app.models.home.SDUI.sdui_data_model import SDUIData

class SDUIComponent:
    def __init__(self, type: str, data: SDUIData, config: SDUIConfig = None):
        self.component_type = type
        self.data = data
        self.config = config
    
    def to_json(self):
        return jsonify(self.__dict__)
    
    
