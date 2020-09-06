import re

from nanohttp import json, HTTPNotFound, HTTPForbidden, validate, \
    int_or_notfound, context
from restfulpy.authorization import authorize
from restfulpy.controllers import ModelRestController
from restfulpy.orm import DBSession, commit

from witch.models.member import Member
from ..exceptions import *

MEMBER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
DATETIME_PATTERN = re.compile(
    r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
    r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
)
MEMBER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')


class MemberController(ModelRestController):

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
        email=dict(
            required=StatusEmailIsRequired,
            not_none=StatusEmailIsNull,
            pattern=(MEMBER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
        password=dict(
            required=HTTPPasswordNotInForm,
            not_none=HTTPPasswordIsNull,
            min_length=(6, HTTPPasswordInvalidLength),
            max_length=(20, HTTPPasswordInvalidLength),
            pattern=(MEMBER_PASSWORD_PATTERN, HTTPPasswordWrongPattern)
        )
    )
    @commit
    def create(self):
        member_title_check = DBSession.query(Member) \
            .filter(Member.title == context.form.get('title')) \
            .one_or_none()
        if member_title_check is not None:
            raise StatusRepetitiveTitle()

        member_email_check = DBSession.query(Member) \
            .filter(Member.email == context.form.get('email')) \
            .one_or_none()
        if member_email_check is not None:
            raise StatusRepetitiveEmail()

        member = Member()
        member.update_from_request()
        DBSession.add(member)
        principal = member.create_jwt_principal()
        context.application.__authenticator__.setup_response_headers(principal)
        return member

    @authorize
    @json
    def get(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()

        return member

    @authorize
    @json
    @Member.expose
    def list(self):
        members = DBSession.query(Member)
        return members

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
        email=dict(
            not_none=StatusEmailIsNull,
            pattern=(MEMBER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
    )
    @commit
    def update(self, id):
        id = int_or_notfound(id)
        current_member_id = context.identity.payload['id']
        if id != current_member_id:
            raise HTTPForbidden()

        member = DBSession.query(Member) \
            .filter(Member.id == id) \
            .one_or_none()
        if member is None:
            raise HTTPNotFound()

        member_title_check = DBSession.query(Member) \
            .filter(Member.id != id) \
            .filter(Member.title == context.form.get('title')) \
            .one_or_none()
        if member_title_check is not None:
            raise StatusRepetitiveTitle()

        member_email_check = DBSession.query(Member) \
            .filter(Member.id != id) \
            .filter(Member.email == context.form.get('email')) \
            .one_or_none()
        if member_email_check is not None:
            raise StatusRepetitiveEmail()

        member.update_from_request()
        return member

    @authorize
    @json
    @commit
    def delete(self, id):
        id = int_or_notfound(id)
        member = DBSession.query(Member).get(id)
        if member is None:
            raise HTTPNotFound()

        DBSession.delete(member)
        return member

