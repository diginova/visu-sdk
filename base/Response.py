import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import encode64
import numpy as np


class Response:
    def __init__(self,request,image):
        self.request = request
        self.image=image
        
    def response(self):
        self.image = encode64(np.asarray(self.image))
        self.data=self.request.get(self.request.Component,"name","uID","imageType")
        return json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": {
            "image": {"imageType": self.data["imageType"], "imageData": self.image}}}]})