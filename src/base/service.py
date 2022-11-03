import json
from sdks.visu.src.base.request import Request


class Service():

    def __init__(self,data,services):
        self.data=json.loads(data)
        self.services=services

    def run(self):
        res = []
        for req in self.data["requests"]:
            component = req["name"]
            req = Request(req)
            res.append(self.services[component](req).run())
        return {"responses":res}