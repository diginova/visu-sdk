# -*- coding: utf-8 -*-

from pydantic import BaseModel
from typing import List, Union,Literal,Optional
import numpy


class TypedArray(numpy.ndarray):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate_type

    @classmethod
    def validate_type(cls, val):
        return numpy.array(val, dtype=cls.inner_type)

class ArrayMeta(type):
    def __getitem__(self, t):
        return type('Array', (TypedArray,), {'inner_type': t})

class Array(numpy.ndarray, metaclass=ArrayMeta):
    pass


class Model(BaseModel):
    """Pydantic Base Model class that is inherited to all classes"""
    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()

class Input(Model):
    name: str
    type: str
    data: list
class Param(Model):
    name: str
    value: str

class RequestModel(Model):
    type: str
    name: str
    uID: str
    params: list
    inputs: list
    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()

class Image(Model):
    name: str
    mime_type: Literal["image/jpg","image/png","image/gif"]
    encoding: Literal["base64"]
    content: Union[str,Array[numpy.float32]]

class BBox(Model):
    x: int
    y: int
    width: int
    height: int

class Output(Model):
    name: str
    type: str
    data: Union[List[Image],List[BBox],int]


class ResponseModel(Model):
    type: str
    name: str
    uID: str
    outputs: List[Output]

    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()

class Requests(Model):
    requests : List[RequestModel]

    def new(cls, *args, **kwargs):
        cls.new = super().new
        return super().construct()
    
