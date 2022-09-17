from typing import List
from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()
    
    
