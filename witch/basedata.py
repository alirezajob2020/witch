from datetime import datetime

from restfulpy.orm import DBSession

from witch.models.user import User


def insert():

    god = User(
        title='GOD',
        first_name='god',
        last_name='godian',
        birth_date=datetime(1, 1, 1),
        email='god@example.com',
        password='Abc123Rew',
    )
    DBSession.add(god)

    user1 = User(
        title='alitk',
        first_name='alireza',
        last_name='tavakoli',
        birth_date=datetime(2000, 5, 2),
        email='ali@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user1)

    user2 = User(
        title='hamiid',
        first_name='hamid',
        last_name='jacob',
        birth_date=datetime(2000, 5, 2),
        email='famil@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user2)

    user3 = User(
        title='rez',
        first_name='reza',
        last_name='ebrahimi',
        birth_date=datetime(2000, 5, 2),
        email='reza@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user3)

    user4 = User(
        title='mamad',
        first_name='mohammad',
        last_name='javadi',
        birth_date=datetime(2000, 5, 2),
        email='mamad@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user4)

    user5 = User(
        title='milawd',
        first_name='milad',
        last_name='ameri',
        birth_date=datetime(2000, 5, 2),
        email='milad@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user5)

    user6 = User(
        title='behroooz',
        first_name='behrouz',
        last_name='pashaei',
        birth_date=datetime(2000, 5, 2),
        email='behrouz@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user6)

    user7 = User(
        title='javati',
        first_name='javad',
        last_name='hashemi',
        birth_date=datetime(2000, 5, 2),
        email='javad@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user7)


    user8 = User(
        title='alifamil',
        first_name='ali',
        last_name='famil',
        birth_date=datetime(2000, 5, 2),
        email='famil@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user8)

    user9 = User(
        title='mehranii',
        first_name='mehran',
        last_name='rezvani',
        birth_date=datetime(2000, 5, 2),
        email='famil@example.com',
        password='Abc123Rew',
    )
    DBSession.add(user9)
    DBSession.commit()

    print('Following user has been added:')
    print(god)
