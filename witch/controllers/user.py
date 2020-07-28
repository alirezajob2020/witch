from nanohttp import json, HTTPNotFound, int_or_notfound, context
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit
from sqlalchemy import exists, and_, or_

from witch.models import User


class UserController(ModelRestController):

    @json
    def create(self):
        user1 = User(
            name="alireza",
            fullname='tavakoli',
            email='alitk@msn.com',
        )

        DBSession.add(user1)
        DBSession.commit()

    @json
    def add(self):
        return "user is added"

    @json
    def delete(self):
        return "user is deleted"

    @json
    def get(self):
        pass
