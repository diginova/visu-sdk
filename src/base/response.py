# -*- coding: utf-8 -*-


class Response:
    def __init__(self, response_model, error=[]):
        self.error = error
        self.response_model = response_model

    def response(self):
        try:
            return  self.response_model.json()
        except (AttributeError,TypeError):
            self.error.append({"error":"hata2"})
            data={'error':self.error}
            return data
