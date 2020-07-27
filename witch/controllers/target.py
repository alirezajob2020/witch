from nanohttp import json, Static
from restfulpy.controllers import ModelRestController


class TargetController(ModelRestController):

    @json
    def create(self):
        return "target is created"

    @json
    def add(self):
        return "target is added"

    @json
    def delete(self):
        return "target is deleted"
