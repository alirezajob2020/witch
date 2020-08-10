import os
import uuid
from hashlib import sha256
from datetime import datetime

from cas import CASPrincipal
from nanohttp import context, settings, HTTPStatus
from restfulpy.orm import DeclarativeBase, Field, DBSession, relationship
from restfulpy.principal import JWTRefreshToken
from sqlalchemy import Unicode, Integer, JSON, Date, UniqueConstraint, String
from sqlalchemy.orm import synonym


class User(DeclarativeBase):
    __tablename__ = 'user'

    id = Field(
        Integer,
        primary_key=True,
        readonly=True,
        not_none=True,
        required=False,
        label='ID',
        minimum=1,
    )
    title = Field(
        String(50)
    )
    first_name = Field(
        String(50),
    )
    last_name = Field(
        String(50),
    )
    birth_date = Field(
        Date,
        python_type=datetime.date,
        label='Birth Date',
        pattern=r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])',
        pattern_description='ISO format like "yyyy-mm-dd" is valid',
        example='2018-02-02',
        watermark='Lorem Ipsum',
        nullable=True,
        not_none=False,
        required=False,
        readonly=False,
    )
    email = Field(
        String,
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
        # Make sure password is a str because we cannot hash unicode objects
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
        return CASPrincipal({
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
