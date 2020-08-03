import re

from nanohttp import json, HTTPNotFound, validate, int_or_notfound, context
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit
from sqlalchemy import exists, and_, or_

from witch.models.user import User
from ..exceptions import *

USER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
DATETIME_PATTERN = re.compile(
    r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
    r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
)


class UserController(ModelRestController):

    @json(
        prevent_empty_form='400 No Parameter Exists In The Form',
    )
    @validate(
        title=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(3, StatusStringLengthInvalid),
            max_length=(256, StatusStringLengthInvalid),
            required=StatusTitleRequired,
            not_none=StatusTitleIsNull,
        ),
        firstname=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastname=dict(
            not_none=StatusLastnameIsNull,
        ),
        birth_date=dict(
            pattern=(DATETIME_PATTERN, StatusInvalidDateFormat),
        ),
        email=dict(
            required=StatusEmailNotInForm,
            not_none=StatusEmailIsNull,
            pattern=(USER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
    )
    @commit
    def create(self):

        query = DBSession.query(User) \
            .filter(User.email == context.form.get('email')) \
            .one_or_none()

        if query is None:
            user = User(
                title=context.form.get('title'),
                firstname=context.form.get('firstname'),
                lastname=context.form.get('lastname'),
                birth_date=context.form.get('birth_date'),
                email=context.form.get('email'),
            )
            DBSession.add(user)
        else:
            raise StatusRepetitiveEmail

        return user
