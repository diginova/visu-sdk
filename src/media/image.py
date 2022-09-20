# -*- coding: utf-8 -*-

import cv2
import base64
import numpy as np
import os

class Image:
    def __init__(self):
        self.image_type = ""
        self.image = []


    def get_img(self, inputs=None):
        print("deneme")
        list_obj = []
        if inputs.type =="image":
            image = Image()
            image.image = list((np.asarray(self.decode64(inputs.image.image_data[0])).astype(np.uint8)))
            image.image_type = inputs.image.mime_type
            list_obj.append(image)
            return list_obj
        elif inputs.type =="image_list":
            for i in range(0,len(inputs.image.image_data)):
                image  = Image()
                image.image = list((np.asarray(self.decode64(inputs.image.image_data[i])).astype(np.uint8)))
                image.image_type = inputs.image.mime_type
                list_obj.append(image)
            return list_obj
        elif inputs.type == "url":
            print(os.listdir(r"/opt/project/components/PreAddNoise/resources"))
            for i in os.listdir(str(inputs.image.image_data[0])):
                image = Image()
                image.image = np.asarray(cv2.imread(str(inputs.image.image_data[0])+"/"+i))
                image.image_type = inputs.image.mime_type
                list_obj.append(image)
            return list_obj


    def encode64(self, image):

        bin = cv2.imencode('.jpg', image)[1]
        data = str(base64.b64encode(bin), "utf-8")
        return data

    def decode64(self, image_data):
        jpg_original = base64.b64decode(image_data)
        image = np.asarray(bytearray(jpg_original), dtype=np.uint8)
        img = cv2.imdecode(image, cv2.IMREAD_COLOR)
        img = np.asarray(img).astype(np.float32)
        return img
