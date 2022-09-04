import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import decode64
import numpy as np


class Request:

    def __init__(self, jsondata):
        self.data = json.loads(jsondata)
        self.model = ""
        self.Component = ""

    def __Index(self):
        self.ComponentIndex = next(
            (index for (index, d) in enumerate(self.model.dict()["components"]) if d['name'] == self.Component), None)
        return self.ComponentIndex

    def getImage(self, component):
        self.Component = component
        return np.asarray(decode64(self.model.components[self.__Index()].inputs.image.imageData)).astype(np.uint8)

    def getParam(self, component):
        self.Component = component
        return self.model.components[self.__Index()].params


    def get(self, component, *args):
        self.Component = component
        returnData= {"component":self.Component}
        print(self.Component)
        for item in args:
            if item=="name":
                returnData[item]=self.model.components[self.__Index()].name
            if item=="uID":
                returnData[item] = self.model.components[self.__Index()].uID
            if item=="image":
                returnData[item] = np.asarray(decode64(self.model.components[self.__Index()].inputs.image.imageData)).astype(np.uint8)
            if item == "params":
                returnData[item] = self.model.components[self.__Index()].params
        return returnData