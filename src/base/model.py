# -*- coding: utf-8 -*-

from typing import List
from pydantic import BaseModel, ValidationError

class Model(BaseModel):
    """Pydantic Base Model class that is inherited to all classes"""
    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()
    
    
