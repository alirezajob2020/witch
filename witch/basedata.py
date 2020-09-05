from datetime import datetime

from restfulpy.orm import DBSession

from witch.models.member import Member


def insert():
    god = Member(
        title='GOD',
        first_name='god',
        last_name='godian',
        gender='male',
        birth_date=datetime(1, 1, 1),
        email='god@example.com',
        password='Abc123Rew',
    )
    DBSession.add(god)

    member1 = Member(
        title='member1',
        first_name='member1',
        last_name='family member1',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member1@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member1)

    member2 = Member(
        title='member2',
        first_name='member2',
        last_name='family member1',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member2@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member2)

    member3 = Member(
        title='member3',
        first_name='member3',
        last_name='family member3',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member3@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member3)

    member4 = Member(
        title='member4',
        first_name='member4',
        last_name='family member4',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member4@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member4)

    member5 = Member(
        title='member5',
        first_name='member5',
        last_name='family member5',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member5@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member5)

    member6 = Member(
        title='member6',
        first_name='member6',
        last_name='family member6',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member6@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member6)

    member7 = Member(
        title='member7',
        first_name='member7',
        last_name='family member7',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member7@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member7)

    member8 = Member(
        title='member8',
        first_name='member8',
        last_name='family member8',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member8@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member8)

    member9 = Member(
        title='member9',
        first_name='member9',
        last_name='family member9',
        gender='male',
        birth_date=datetime(2000, 5, 2),
        email='member9@example.com',
        password='Abc123Rew',
    )
    DBSession.add(member9)
    DBSession.commit()

    print('Following member has been added:')
    print(god)

