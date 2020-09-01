from datetime import datetime

from restfulpy.orm import DBSession

from witch.models.member import Member


def insert():
    user1 = Member(
        title='mock user1',
        first_name='user1',
        last_name='family user1',
        birth_date=datetime(1, 1, 1),
        email='user1@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user1)

    user2 = Member(
        title='mock user2',
        first_name='user2',
        last_name='family user2',
        birth_date=datetime(2000, 5, 2),
        email='user2@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user2)

    user3 = Member(
        title='mock user3',
        first_name='user3',
        last_name='family user3',
        birth_date=datetime(2000, 5, 2),
        email='user3@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user3)

    user4 = Member(
        title='mock user4',
        first_name='user4',
        last_name='family user4',
        birth_date=datetime(2000, 5, 2),
        email='user4@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user4)

    user5 = Member(
        title='mock user5',
        first_name='user5',
        last_name='family user5',
        birth_date=datetime(2000, 5, 2),
        email='user5@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user5)

    user6 = Member(
        title='mock user6',
        first_name='user6',
        last_name='family user6',
        birth_date=datetime(2000, 5, 2),
        email='user6@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user6)

    user7 = Member(
        title='mock user7',
        first_name='user7',
        last_name='family user7',
        birth_date=datetime(2000, 5, 2),
        email='user7@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user7)

    user8 = Member(
        title='mock user8',
        first_name='user8',
        last_name='family user8',
        birth_date=datetime(2000, 5, 2),
        email='user@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user8)

    user9 = Member(
        title='mock user9',
        first_name='user9',
        last_name='family user9',
        birth_date=datetime(2000, 5, 2),
        email='user9@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user9)

    user10 = Member(
        title='mock user10',
        first_name='user10',
        last_name='family user10',
        birth_date=datetime(2000, 5, 2),
        email='user10@msn.com',
        password='Abc123Rew',
    )
    DBSession.add(user10)
    DBSession.commit()

