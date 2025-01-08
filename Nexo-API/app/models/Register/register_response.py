from flask import jsonify

class RegisterResponse:
    def __init__(self, message, token):
        self.message = message
        self.token = token

    def to_json(self):
        return jsonify(self.__dict__)