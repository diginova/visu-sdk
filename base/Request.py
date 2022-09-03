
import json
from sdks.visu.base.Model import Model

class Request:
    def __init__(self, jsondata):
        self.data = json.loads(jsondata)
        self.model=""
        
    def get(self,name):
        return self.model.name
        

    

