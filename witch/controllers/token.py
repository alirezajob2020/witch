import re

from nanohttp import RestController, json, validate, context
from restfulpy.authorization import authorize

from ..exceptions import HTTPIncorrectEmailOrPassword, StatusEmailIsRequired, \
    StatusEmailIsNull, StatusInvalidEmailFormat

USER_EMAIL_PATTERN = re.compile(
    r'(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)'
)
DATETIME_PATTERN = re.compile(
    r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
    r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
)
USER_PASSWORD_PATTERN = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+')


class TokenController(RestController):

    @json(prevent_empty_form=True)
    @validate(
        email=dict(
            required=StatusEmailIsRequired,
            not_none=StatusEmailIsNull,
            pattern=(USER_EMAIL_PATTERN, StatusInvalidEmailFormat),
        ),
        password=dict(
            required='400 Password Not In Form',
            not_none='400 Password is null',
            min_length=(6, '400 Invalid Password Length'),
            max_length=(20, '400 Invalid Password Length'),
            pattern=(USER_PASSWORD_PATTERN, '400 Password Not Complex Enough')
        )
    )
    def create(self):
        email = context.form.get('email')
        password = context.form.get('password')
        if email and password is None:
            raise HTTPIncorrectEmailOrPassword()

        principal = context.application.__authenticator__. \
            login((email, password))

        print(principal)

        if principal is None:
            raise HTTPIncorrectEmailOrPassword()

        return dict(token=principal.dump())
