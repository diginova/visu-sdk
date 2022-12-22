import json
from sdks.visu.src.base.request import Request


class Service():

    def __init__(self,data,services,load):
        self.data=json.loads(data)
        self.services=services
        self.load=load

    def run(self):
        res = []
        for req in self.data["requests"]:
            component = req["name"]
            req = Request(req)

            if self.load.get(component):
                res.append(self.services[component](req, self.load[component]).run())

            else:
                res.append(self.services[component](req).run())
        return {"responses":res}

class Bootstrap():
    def __init__(self, services):
        self.services = services

    def bootStrap(self):
        bootStrap= {}
        for key, value in self.services.items():
            if key=="facedetection" or key=="objectdetection" or key=="aifacedetection" or key=="aifacerecognition":
                bootStrap[key] = value.bootstrap()
        return bootStrap