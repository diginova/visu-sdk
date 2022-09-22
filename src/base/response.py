# -*- coding: utf-8 -*-

import json
import numpy as np
from sdks.visu.src.media.image import Image
import cv2


class Response:
    def __init__(self, image, request, ResponseModel):
        self.data = {}
        self.request = request
        self.image = image
        self.ResponseModel = ResponseModel

    def response(self):
        list = []
        if self.request.model.inputs.type == "image" or self.request.model.inputs.type =="image_list"or self.request.model.inputs.type =="path":
            for i in range(0,len(self.image)):
                list.append( Image().encode64(np.asarray(self.image[i].image).astype(np.float32), self.image[i].image_type))
                self.mime_type=self.image[i].image_type
            self.data = self.request.get("name", "uID", "imageType")
            data = (json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": \
                {"type": self.request.model.inputs.type,"image": {"mime_type":   self.mime_type, "image_data":list }}}]}))
            data = json.loads(data)
            return self.ResponseModel(**data).dict()
        elif self.request.model.inputs.type == "url":
            url_list=[]
            url_list.append(self.request.model.inputs.image.image_data[0])
            for i in range(0, len(self.image)):
                writeImage = self.request.model.inputs.image.image_data[0] + "/" "changed"+ str(i) +"."+ str(self.image[i].image_type)
                cv2.imwrite(writeImage, np.asarray(self.image[i].image))
                self.mime_type = self.image[i].image_type
                self.data = self.request.get("name", "uID", "imageType")
            data = (json.dumps({"components": [{"name": self.data["name"], "uID": self.data["uID"], "outputs": \
                {"type": self.request.model.inputs.type, "image": {"mime_type": self.mime_type, "image_data": url_list}}}]}))
            data = json.loads(data)
            return self.ResponseModel(**data).dict()
