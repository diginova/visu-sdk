from abc import abstractmethod


class Component:
    @abstractmethod
    def __init__(self, request):
        self.request = request

    @abstractmethod
    def run(self):
        return []
