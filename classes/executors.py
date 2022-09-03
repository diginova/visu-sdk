# -*- coding: utf-8 -*-
"""Abstract base class"""

from abc import ABC, abstractmethod




class BaseClass():
    """Abstract  class that is inherited to all classes"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def run(self):
        pass
