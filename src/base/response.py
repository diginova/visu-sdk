# -*- coding: utf-8 -*-

import json
import numpy as np
from visu.sdk.media.image import Image


class Response:
    def __init__(self, image, request, ResponseModel):
        self.data = {}
        self.request = request
        self.image = image
        self.ResponseModel = ResponseModel

    def response(self):
        list = []
        for i in range(0,len(self.image)):
            list.append( Image().encode64(np.asarray(self.image[i].image).astype(np.float32)))
            mime_type=self.image[i].image_type
        self.data = self.request.get("name", "uID", "imageType")
        data = (json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": \
            {"type": self.request.model.inputs.type,"image": {"mime_type": mime_type, "image_data":list }}}]}))
        data = json.loads(data)
        return self.ResponseModel(**data).dict()
