from datetime import datetime, timedelta

from nanohttp.contexts import Context
from restfulpy.testing import db

from witch.models.member import Member


def test_age(db):
    session = db()

    user1 = Member(
        title='alireza',
        email='alitk@gmail.com',
        first_name='ali',
        last_name='tavakoli',
        birth_date='1970-2-2',
        password='Ali123',
    )

    session.add(user1)
    session.commit()

    user1 = session.query(Member).filter(Member.id == user1.id)