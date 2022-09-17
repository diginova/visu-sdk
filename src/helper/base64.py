# -*- coding: utf-8 -*-

import cv2
import base64
import numpy as np


class Base64(base64):

    def encode64(image):
        bin = cv2.imencode('.jpg', image)[1]
        data = str(base64.b64encode(bin), "utf-8")
        return data

    def decode64(image_data):
        jpg_original = base64.b64decode(image_data)
        image = np.asarray(bytearray(jpg_original), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        img = np.asarray(img).astype(np.float32)
        return img
