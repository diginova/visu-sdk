from typing import List
from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    def __init__(self,data):
        super().__init__(**data)
    
    
