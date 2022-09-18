# -*- coding: utf-8 -*-

import json
import numpy as np
from visu.sdk.media.image import Image


class Response:
    def __init__(self, image, request, ResponseModel):
        self.data = {}
        self.request = request
        self.image = np.asarray(image).astype(np.float32)
        self.ResponseModel = ResponseModel

    def response(self):
        self.data = self.request.get("name", "uID", "imageType")
        data = (json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": {
            "image": {"imageType": self.data["imageType"], "imageData": Image.encode64(self.image)}}}]}))
        data = json.loads(data)
        return self.ResponseModel(**data).dict()
