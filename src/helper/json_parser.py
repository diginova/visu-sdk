# -*- coding: utf-8 -*-

import json
import numpy as np
from visu.Image.base64 import encode64, decode64



class JsonParser:
    def __init__(self, json_data):
        self.jsondata = json.loads(json_data)
        self.request = self.jsondata["components"]

    def getimage(self):
        for i in range(0, len(self.request)):
            self.imageData = self.request[i]["inputs"]["image"]
        if self.imageData["imageType"] == "Base64":
            self.image = np.asarray(decode64(self.imageData["imageData"])).astype(np.uint8)
            return self.image

    def params(self):
        for i in range(0, len(self.request)):
            self.params = self.request[i]["params"]
        return self.params

    def returnJson(self, image):
        image = encode64(np.asarray(image))
        for i in range(0, len(self.request)):
            return json.dumps({"components": [{"name": self.request[i]["name"], "uID": self.request[i]["uID"],
                                               "outputs": {"image": {
                                                   "imageType": self.request[i]["inputs"]["image"]["imageType"],
                                                   "imageData": image}}}]})
