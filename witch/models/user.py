import os
import uuid
from datetime import datetime
from hashlib import sha256

from restfulpy.principal import JWTPrincipal
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin
from restfulpy.principal import JWTRefreshToken
from sqlalchemy import Integer, func, DateTime, String, \
    Unicode
from sqlalchemy.orm import synonym, column_property


class User(DeclarativeBase, OrderingMixin, FilteringMixin, PaginationMixin):
    __tablename__ = 'user'

    id = Field(
        Integer,
        primary_key=True,
        readonly=True,
        required=False,
        not_none=True,
        label='ID',
        minimum=1,
    )
    title = Field(
        String(50)
        required=True,
        not_none=True,
        readonly=False,
        label='Title',
    )
    first_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='First Name',
    )
    last_name = Field(
        String(50),
        required=True,
        not_none=True,
        readonly=False,
        label='Last Name',
    )
    birth_date = Field(
        DateTime,
        python_type=datetime,
        pattern=r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])',
        pattern_description='ISO format like "yyyy-mm-dd" is valid',
        example='2018-02-02',
        watermark='Lorem Ipsum',
        nullable=True,
        not_none=False,
        required=False,
        readonly=False,
        label='Birth Date',
    )

    age = column_property(
        ((func.date(func.now()) - birth_date.label('age')) / 365)
    )
    email = Field(
        String,
        required=True,
        not_none=True,
        readonly=False,
        label='Email',
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

