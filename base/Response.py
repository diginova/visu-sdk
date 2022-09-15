import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import encode64
import numpy as np
from sdks.visu.base.Request import Request

class Response:
    def __init__(self,image , request , ResponseModel):
        self.request = request
        self.image = np.asarray(image).astype(np.float32)
        self.ResponseModel=ResponseModel


    def response(self):
        self.data=self.request.get("name","uID","imageType")
        data=(json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": {
            "image": {"imageType": self.data["imageType"], "imageData": encode64(self.image)}}}]}))
        data=json.loads(data)
        return self.ResponseModel(**data).dict()