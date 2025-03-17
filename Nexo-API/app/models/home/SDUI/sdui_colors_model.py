from flask import jsonify

class SDUIColors:
    def __init__(self, background: str = None, borderColor=None, textColor=None, iconColor=None):
        self.background = background
        self.borderColor = borderColor
        self.textColor = textColor
        self.iconColor = iconColor

    def to_json(self):
        return jsonify(self.__dict__)