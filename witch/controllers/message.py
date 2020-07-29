from nanohttp import json, Static
from restfulpy.controllers import ModelRestController


class MessageController(ModelRestController):

    @json
    def create(self):
        pass

    @json
    def delete(self):
        pass
