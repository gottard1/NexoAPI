from flask import jsonify

class RegisterFailure:
    def __init__(self, message):
        self.message = message

    def to_json(self):
        return jsonify(self.__dict__)