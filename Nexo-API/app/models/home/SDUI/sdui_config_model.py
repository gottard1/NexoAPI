from flask import jsonify
from app.models.home.SDUI.sdui_spacing_model import SDUISpacing
from app.models.home.SDUI.sdui_colors_model import SDUIColors

class SDUIConfig:
    def __init__(self, colors: SDUIColors = None, spacing: SDUISpacing = None):
        self.colors = colors
        self.spacing = spacing

    def to_json(self):
        return jsonify(self.__dict__)