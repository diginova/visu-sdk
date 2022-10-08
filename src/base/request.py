# -*- coding: utf-8 -*-


from visu.sdk.media.image import Image


class Request:

    def __init__(self, json_data):
        try:
            self.data = json_data
            self.model = ""
            self.image = []
        except TypeError as e:
            print("error",e)


    def get_inputs(self):
        new = Image()
        self.image = new.get_inputs(inputs=self.model.inputs)
        if self.image==None:
            return {"error":"Image error"}
        return self.image


    def get_input(self,name):
        return [inp for inp in self.model.inputs if name in inp.name][0]


    def get_param(self,name):
        return [par for par in self.model.params if name in par.name][0]

    def get_name(self):
        return self.model.name

    def get_uID(self):
        return self.model.uID

    def get_type(self):
        return self.model.type

