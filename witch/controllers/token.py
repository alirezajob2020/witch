import re

from nanohttp import RestController, json, validate, context
from restfulpy.authorization import authorize

from ..exceptions import HTTPIncorrectEmailOrPassword, StatusEmailIsRequired, \
    StatusEmailIsNull, StatusInvalidEmailFormat, HTTPPasswordNotInForm, \
    HTTPPasswordIsNull, HTTPPasswordInvalidLength, HTTPPasswordWrongPattern

USER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
DATETIME_PATTERN = re.compile(
    r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
    r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
)
USER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')


class TokenController(RestController):

    @json(prevent_empty_form='400 Empty Form')
    @validate(
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
    def create(self):
        email = context.form.get('email')
        password = context.form.get('password')
        if email and password is None:
            raise HTTPIncorrectEmailOrPassword()

        principal = context.application.__authenticator__. \
            login((email, password))

        if principal is None:
            raise HTTPIncorrectEmailOrPassword()

        return dict(token=principal.dump())
