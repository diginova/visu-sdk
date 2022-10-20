# -*- coding: utf-8 -*-

import cv2
import base64
import numpy as np
from visu.sdk.base.model import Image as ImageModel


class Image:
    @staticmethod
    def get_images(data):
        list_obj = []
        for img in data:
            content=np.asarray(Image.decode64(img.content))
            image = ImageModel(name=img.name,mime_type=img.mime_type,encoding=img.encoding,content=content)
            list_obj.append(image)
        return list_obj

    @staticmethod
    def encode64(image,mime_type):
        mime_type=mime_type.split("/")
        bin = cv2.imencode("."+str(mime_type[1]), image)[1]
        data = str(base64.b64encode(bin), "utf-8")
        return data

    @staticmethod
    def decode64( image_data):
        b64_decoded_img = base64.b64decode(image_data)
        image = np.asarray(bytearray(b64_decoded_img), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return img
