from datetime import datetime

from restfulpy.orm import DBSession

from witch.models.user import User


def insert():
    user1 = User(
        title='user1',
        first_name='user1',
        last_name='family user1',
        birth_date=datetime.now() - 1200,
        email='user1@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user1)

    user2 = User(
        title='user2',
        first_name='user2',
        last_name='family user2',
        birth_date=datetime.now() - 1200,
        email='user2@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user2)

    user3 = User(
        title='user3',
        first_name='user3',
        last_name='family user3',
        birth_date=datetime.now() - 1200,
        email='user3@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user3)

    user4 = User(
        title='user4',
        first_name='user4',
        last_name='family user4',
        birth_date=datetime.now() - 1200,
        email='user4@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user4)

    user5 = User(
        title='user5',
        first_name='user5',
        last_name='family user5',
        birth_date=datetime.now() - 1200,
        email='user5@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user5)

    user6 = User(
        title='user6',
        first_name='user6',
        last_name='family user6',
        birth_date=datetime.now() - 1200,
        email='user6@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user6)

    user7 = User(
        title='user7',
        first_name='user7',
        last_name='family user7',
        birth_date=datetime.now() - 1200,
        email='user7@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user7)

    user8 = User(
        title='user8',
        first_name='user8',
        last_name='family user8',
        birth_date=datetime.now() - 1200,
        email='user8@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user8)

    user9 = User(
        title='user9',
        first_name='user9',
        last_name='family user9',
        birth_date=datetime.now() - 1200,
        email='user9@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user9)

    user10 = User(
        title='user10',
        first_name='user10',
        last_name='family user10',
        birth_date=datetime.now() - 1200,
        email='user10@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user10)

    user11 = User(
        title='user11',
        first_name='user11',
        last_name='family user11',
        birth_date=datetime.now() - 1200,
        email='user11@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user11)

    user12 = User(
        title='user12',
        first_name='user12',
        last_name='family user12',
        birth_date=datetime.now() - 1200,
        email='user12@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user12)

    user13 = User(
        title='user13',
        first_name='user13',
        last_name='family user13',
        birth_date=datetime.now() - 1200,
        email='user13@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user13)

    user14 = User(
        title='user14',
        first_name='user14',
        last_name='family user14',
        birth_date=datetime.now() - 1200,
        email='user14@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user14)

    user15 = User(
        title='user15',
        first_name='user15',
        last_name='family user15',
        birth_date=datetime.now() - 1200,
        email='user15@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user15)

    user16 = User(
        title='user16',
        first_name='user16',
        last_name='family user16',
        birth_date=datetime.now() - 1200,
        email='user16@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user16)

    user17 = User(
        title='user17',
        first_name='user17',
        last_name='family user17',
        birth_date=datetime.now() - 1200,
        email='user17@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user17)

    user18 = User(
        title='user18',
        first_name='user18',
        last_name='family user18',
        birth_date=datetime.now() - 1200,
        email='user18@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user18)

    user19 = User(
        title='user19',
        first_name='user19',
        last_name='family user19',
        birth_date=datetime.now() - 1200,
        email='user19@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user19)

    user20 = User(
        title='user20',
        first_name='user20',
        last_name='family user20',
        birth_date=datetime.now() - 1200,
        email='user20@gmail.com',
        password='Abc123Rez',
    )
    DBSession.add(user20)
    DBSession.commit()


