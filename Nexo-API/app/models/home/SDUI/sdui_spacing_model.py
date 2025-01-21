from flask import jsonify

class SDUISpacing:
    def __init__(self, topSpacer: float = None, leadingSpacer: float = None, traillingSpacer: float = None, bottomSpacer: float = None):
        self.topSpacer = topSpacer
        self.leadingSpacer = leadingSpacer
        self.traillingSpacer = traillingSpacer
        self.bottomSpacer = bottomSpacer

    def to_json(self):
        return jsonify(self.__dict__)