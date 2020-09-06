import os
import uuid
import datetime
from hashlib import sha256

from restfulpy.principal import JWTPrincipal
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin
from restfulpy.principal import JWTRefreshToken
from sqlalchemy import Integer, func, DateTime, Enum, String, \
    Unicode
from sqlalchemy.orm import synonym, column_property

genders = [
    'male',
    'female',
]


class Member(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'member'

    id = Field(
        Integer,
        primary_key=True,
        unique=True,
        required=True,
        not_none=True,
        readonly=True,
        label='ID',
        minimum=1,
    )
    title = Field(
        String(50),
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='Title',
        example='alitk',
    )
    first_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='First Name',
        example='alireza',
    )
    last_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='Last Name',
        example='tavakoli',
    )
    gender = Field(
        Enum(*genders, name='genders'),
        python_type=str,
        not_none=False,
        required=True,
        readonly=False,
        label='gender',
        watermark='Choose Your Gender',
        example='male',
    )
    email = Field(
        String,
        unique=True,
        required=True,
        not_none=True,
        readonly=False,
        label='Email',
        example='alitk@gmail.com',
    )
    _password = Field(
        'password',
        Unicode(128),
        index=True,
        protected=True,
        json='password',
        pattern=r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).+$',
        pattern_description='Password must include at least one uppercase, one'
            'lowercase and one number',
        example='ABCabc123',
        watermark=None,
        label='Password',
        message=None,
        min_length=6,
        max_length=20,
        required=True,
        python_type=str,
        not_none=True,
    )

    def _hash_password(cls, password):
        salt = sha256()
        salt.update(os.urandom(60))
        salt = salt.hexdigest()

        hashed_pass = sha256()
        hashed_pass.update((password + salt).encode('utf-8'))
        hashed_pass = hashed_pass.hexdigest()

        password = salt + hashed_pass
        return password

    def _set_password(self, password):
        """Hash ``password`` on the fly and store its hashed version."""
        self._password = self._hash_password(password)

    def _get_password(self):
        """Return the hashed version of the password."""
        return self._password

    password = synonym(
        '_password',
        descriptor=property(_get_password, _set_password),
        info=dict(protected=True)
    )

    def create_jwt_principal(self):
        return JWTPrincipal({
            'id': self.id,
            'title': self.title,
            'email': self.email,
            'firstName': self.first_name,
            'lastName': self.last_name,
            'sessionId': str(uuid.uuid4()),
        })

    def create_refresh_principal(self):
        return JWTRefreshToken(dict(id=self.id))

    def validate_password(self, password):
        hashed_pass = sha256()
        hashed_pass.update((password + self.password[:64]).encode('utf-8'))
        return self.password[64:] == hashed_pass.hexdigest()

