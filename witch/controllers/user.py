from nanohttp import json, HTTPNotFound, int_or_notfound, context
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit
from sqlalchemy import exists, and_, or_

from witch.models.user import User


class UserController(ModelRestController):

    @json
    @commit
    def create(self):
        user = User(
            name=context.form.get('name'),
            fullname=context.form.get('fullname'),
            email=context.form.get('email'),
        )

        DBSession.add(user)

        return user
