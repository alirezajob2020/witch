from nanohttp import json, Static
from restfulpy.controllers import ModelRestController


class TargetController(ModelRestController):

    @json
    def create(self):
        pass

    @json
    def delete(self):
        pass
