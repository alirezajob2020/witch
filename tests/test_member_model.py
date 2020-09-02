from datetime import datetime, timedelta

from nanohttp.contexts import Context
from restfulpy.testing import db

from witch.models.member import Member


def test_age(db):
    session = db()

    member1 = Member(
        title='alireza',
        email='alitk@gmail.com',
        first_name='ali',
        last_name='tavakoli',
        birth_date='1970-2-2',
        password='Ali123',
    )

    session.add(member1)
    session.commit()

    member1 = session.query(Member).filter(Member.id == member1.id)

