import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import decode64
import numpy as np


class Request:

    def __init__(self, json_data, component):
        self.component = component
        json_data_deneme = json.loads(json_data)
        self.data = json_data_deneme["components"][next(
            (index for (index, d) in enumerate(json_data_deneme["components"]) if d['name'] == self.component), None)]
        self.model = ""
        self.image = self.get_image()

    def get_image(self):
        try:
            if self.model.inputs.image.imageType == "base64":
                return np.asarray(decode64(self.model.inputs.image.imageData)).astype(np.uint8)

        except AttributeError:
            return None

    def get_url(self):
        try:
            if self.model.inputs.image.imageType == "URL":
                return self.model.inputs.image.imageData

        except AttributeError:
            return None

    def get_param(self):
        return self.model.params

    def get_uID(self):
        return self.model.inputs.image.imageType



    def get(self, *args):
        returnData= {"component":self.component}
        for item in args:
            if item=="name":
                returnData[item]=self.model.name
            if item=="uID":
                returnData[item] = self.model.uID
            if item=="image":
                returnData[item] = np.asarray(decode64(self.model.inputs.image.imageData)).astype(np.uint8)
            if item == "params":
                returnData[item] = self.model.params
            if item == "imageType":
                returnData[item] = self.model.inputs.image.imageType
        return returnData