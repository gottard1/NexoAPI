from flask import jsonify

class SDUIData:
    def __init__(self, title: str = None, description: str = None, value: float = None, action: str = None, icon: str = None):
        self.title = title
        self.description = description
        self.value = value
        self.action = action
        self.icon = icon

    def to_json(self):
        return jsonify(self.__dict__)