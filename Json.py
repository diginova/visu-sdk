import json
from sdks.visu.base64 import encode64
import numpy as np

class Json:
    def __init__(self,json_data):
        self.jsondata = json.loads(json_data)
        self.request = self.jsondata["capsules"]

    def image(self):
        for i in range(0, len(self.request)):
            self.imageData = self.request[i]["inputs"]["image"]
        if self.imageData["imageType"] == "Base64":
            return self.imageData["imageData"]

    def params(self):
        for i in range(0, len(self.request)):
            self.params=self.request[i]["params"]
        return self.params

    def returnJson(self,image):
        for i in range(0, len(self.request)):
            return json.dumps({"capsules": [{"name":self.request[i]["name"],"uID": self.request[i]["uID"],"outputs":{"image": {"imageType": self.request[i]["inputs"]["image"]["imageType"],"imageData":image }}}]})

