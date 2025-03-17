from flask import jsonify

class HomeComponents:
    def __init__(self, components: list):
        self.components = components

    def to_json(self):
        return jsonify(self.__dict__)