import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import decode64
import numpy as np


class Request:

    def __init__(self, jsondata):
        self.data = json.loads(jsondata)
        self.model = ""
        self.component = ""

    def __Index(self):
        self.ComponentIndex = next(
            (index for (index, d) in enumerate(self.model.dict()["components"]) if d['name'] == self.Component), None)
        return self.ComponentIndex

    def getImage(self):
        return np.asarray(decode64(self.model.components[self.__Index()].inputs.image.imageData)).astype(np.uint8)

    def getParam(self):
        return self.model.components[self.__Index()].params

    def getuID(self):
        return self.model.components[self.__Index()].inputs.image.imageType



    def get(self, *args):
        returnData= {"component":self.Component}
        for item in args:
            if item=="name":
                returnData[item]=self.model.components[self.__Index()].name
            if item=="uID":
                returnData[item] = self.model.components[self.__Index()].uID
            if item=="image":
                returnData[item] = np.asarray(decode64(self.model.components[self.__Index()].inputs.image.imageData)).astype(np.uint8)
            if item == "params":
                returnData[item] = self.model.components[self.__Index()].params
            if item == "imageType":
                returnData[item] = self.model.components[self.__Index()].inputs.image.imageType
        return returnData