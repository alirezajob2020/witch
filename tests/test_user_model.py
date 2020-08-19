from datetime import datetime, timedelta

from nanohttp import settings
from nanohttp import context
from nanohttp.contexts import Context
from restfulpy.testing import db
from auditor.context import Context as AuditLogContext

from witch.models.user import User


def test_age(db):
    session = db()

    user1 = User(
        title='alireza',
        email='alitk@gmail.com',
        first_name='ali',
        last_name='tavakoli',
        birth_date='1970-2-2',
        password='Ali123',
    )

    session.add(user1)
    session.commit()

    user1 = session.query(User).filter(User.id == user1.id)