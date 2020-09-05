from datetime import datetime

from restfulpy.orm import DBSession

from witch.models.member import Member


def insert():
    member1 = Member(
        title='mock member1',
        first_name='member1',
        last_name='family member1',
        gender='male',
        birth_date=datetime(1, 1, 1),
        email='member1@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member1)

    member2 = Member(
        title='mock member2',
        first_name='member2',
        last_name='family member2',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member2@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member2)

    member3 = Member(
        title='mock member3',
        first_name='member3',
        last_name='family member3',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member3@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member3)

    member4 = Member(
        title='mock member4',
        first_name='member4',
        last_name='family member4',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member4@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member4)

    member5 = Member(
        title='mock member5',
        first_name='member5',
        last_name='family member5',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member5@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member5)

    member6 = Member(
        title='mock member6',
        first_name='member6',
        last_name='family member6',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member6@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member6)

    member7 = Member(
        title='mock member7',
        first_name='member7',
        last_name='family member7',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member7@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member7)

    member8 = Member(
        title='mock member8',
        first_name='member8',
        last_name='family member8',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member8)

    member9 = Member(
        title='mock member9',
        first_name='member9',
        last_name='family member9',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member9@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member9)

    member10 = Member(
        title='mock member10',
        first_name='member10',
        last_name='family member10',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member10@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(member10)
    DBSession.commit()

