# -*- coding: utf-8 -*-
import json

class Response:
    def __init__(self, response_model, error=[]):
        self.error = error
        self.response_model = response_model

    def response(self):
        try:
            self.response_model = json.loads(self.response_model.json())
            return self.response_model
        except (AttributeError,TypeError):
            self.error.append({"error":"hata2"})
            data={'error':self.error}
            return data
