
import json
from sdks.visu.base.Model import Model
from sdks.visu.Image.base64 import decode64
import numpy as np

class Request:
    def __init__(self, jsondata):
        self.data = json.loads(jsondata)
        self.model=""
        
    def get(self):
        return  np.asarray(decode64(self.model.components[0].inputs.image.imageData)).astype(np.uint8)
        

    

