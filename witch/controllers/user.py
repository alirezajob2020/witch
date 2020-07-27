from nanohttp import json, Static
from restfulpy.controllers import ModelRestController


class UserController(ModelRestController):

    @json
    def create(self):
        return "user is created"

    @json
    def add(self):
        return "user is added"

    @json
    def delete(self):
        return "user is deleted"
