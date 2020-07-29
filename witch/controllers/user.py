from nanohttp import json, HTTPNotFound, int_or_notfound, context
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit
from sqlalchemy import exists, and_, or_

from witch.models.user import User


class UserController(ModelRestController):

    @json
    def create(self):
        user1 = User(
            name='alireza',
            fullname='tavakoli',
            email='alitk@msn.com',
        )

        DBSession.add(user1)
        DBSession.commit()

        return user1

    @json
    def get(self, id):
        user1 = DBSession.query(User) \
            .filter(User.id == id).one_or_none()

        return user1

    @json
    def delete(self):
        pass
