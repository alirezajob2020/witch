import re

from nanohttp import json, HTTPNotFound, HTTPForbidden, validate, \
    int_or_notfound, context
from restfulpy.authorization import authorize
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit

from witch.models.user import User
from ..exceptions import *

USER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
DATETIME_PATTERN = re.compile(
    r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
    r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
)
USER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')


class UserController(ModelRestController):

    @json(
        prevent_empty_form='400 No Parameter Exists In The Form',
    )
    @validate(
        title=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(3, StatusTitleLengthInvalid),
            max_length=(256, StatusTitleLengthInvalid),
            required=StatusTitleIsRequired,
            not_none=StatusTitleIsNull,
        ),
        firstName=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastName=dict(
            not_none=StatusLastnameIsNull,
        ),
        birthDate=dict(
            pattern=(DATETIME_PATTERN, StatusInvalidDateFormat),
        ),
        email=dict(
            required=StatusEmailIsRequired,
            not_none=StatusEmailIsNull,
            pattern=(USER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
        password=dict(
            required=HTTPPasswordNotInForm,
            not_none=HTTPPasswordIsNull,
            min_length=(6, HTTPPasswordInvalidLength),
            max_length=(20, HTTPPasswordInvalidLength),
            pattern=(USER_PASSWORD_PATTERN, HTTPPasswordWrongPattern)
        )
    )
    @commit
    def create(self):
        user_title_check = DBSession.query(User) \
            .filter(User.id != id) \
            .filter(User.title == context.form.get('title')) \
            .one_or_none()
        if user_title_check is not None:
            raise StatusRepetitiveTitle()

        user_email_check = DBSession.query(User) \
            .filter(User.id != id) \
            .filter(User.email == context.form.get('email')) \
            .one_or_none()
        if user_email_check is not None:
            raise StatusRepetitiveEmail()

        user = User()
        user.update_from_request()
        DBSession.add(user)
        principal = user.create_jwt_principal()
        context.application.__authenticator__.setup_response_headers(principal)
        return user

    @authorize
    @json
    def get(self, id):
        id = int_or_notfound(id)
        user = DBSession.query(User).get(id)
        if user is None:
            raise HTTPNotFound()

        return user

    @authorize
    @json
    @User.expose
    def list(self):
        users = DBSession.query(User)
        return users

    @authorize
    @json
    @validate(
        title=dict(
            type_=(str, StatusInvalidStringType),
            min_length=(3, StatusTitleLengthInvalid),
            max_length=(256, StatusTitleLengthInvalid),
            not_none=StatusTitleIsNull,
        ),
        firstName=dict(
            not_none=StatusFirstnameIsNull,
        ),
        lastName=dict(
            not_none=StatusLastnameIsNull,
        ),
        birthDate=dict(
            pattern=(DATETIME_PATTERN, StatusInvalidDateFormat),
        ),
        email=dict(
            not_none=StatusEmailIsNull,
            pattern=(USER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
    )
    @commit
    def update(self, id):
        id = int_or_notfound(id)
        current_user_id = context.identity.payload['id']
        if id != current_user_id:
            raise HTTPForbidden()

        user = DBSession.query(User) \
            .filter(User.id == id) \
            .one_or_none()
        if user is None:
            raise HTTPNotFound()

        user_title_check = DBSession.query(User) \
            .filter(User.id != id) \
            .filter(User.title == context.form.get('title')) \
            .one_or_none()
        if user_title_check is not None:
            raise StatusRepetitiveTitle()

        user_email_check = DBSession.query(User) \
            .filter(User.id != id) \
            .filter(User.email == context.form.get('email')) \
            .one_or_none()
        if user_email_check is not None:
            raise StatusRepetitiveEmail()

        user.update_from_request()
        return user

    @authorize
    @json
    @commit
    def delete(self, id):
        id = int_or_notfound(id)
        user = DBSession.query(User).get(id)
        if user is None:
            raise HTTPNotFound()

        DBSession.delete(user)
        return user

