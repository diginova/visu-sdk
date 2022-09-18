# -*- coding: utf-8 -*-

import json
import numpy as np
from visu.sdk.base.model import Model
from visu.sdk.media.image import Image
from visu.sdk.helper.base64 import Base64


class Request:

    def __init__(self, json_data, component):
        self.component = component
        self.json_data = json.loads(json_data)
        self.data = self.json_data["components"][next(
            (index for (index, d) in enumerate(self.json_data["components"]) if d['name'] == self.component), None)]
        self.model = ""
        self.image = []

    def get_image(self):
        new = Image()
        self.image = new.get_img(inputs=self.model.inputs)
        return self.image

    def get_param(self):
        return self.model.params

    def get(self, *args):
        returnData= {"component":self.component}
        for item in args:
            if item == "name":
                returnData[item]=self.model.name
            if item == "uID":
                returnData[item] = self.model.uID
            if item == "image":
                returnData[item] = np.asarray(Base64.decode64(self.model.inputs.image.image_data)).astype(np.uint8)
            if item == "params":
                returnData[item] = self.model.params
            if item == "imageType":
                returnData[item] = self.model.inputs.image.mime_type
        return returnData