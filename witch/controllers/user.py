from nanohttp import json, HTTPNotFound, int_or_notfound, context
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit
from sqlalchemy import exists, and_, or_

from witch.models.user import User


class UserController(ModelRestController):

    @json
    def create(self):
        user = User(
            name=context.form['username'],
            fullname=context.form['family'],
            email=context.form['email'],
        )

        DBSession.add(user)
        DBSession.commit()

        return user

    
