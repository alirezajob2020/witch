from nanohttp import json, Static
from restfulpy.controllers import ModelRestController


class MessageController(ModelRestController):

    @json
    def create(self):
        return "new message is created"

    @json
    def add(self):
        return "new message is added"

    @json
    def delete(self):
        return "message is deleted"
