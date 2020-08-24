from restfulpy.orm import DBSession

from witch.models.user import User


def insert():

    god = User(
        title='GOD',
        first_name='god',
        last_name='godian',
        birth_date='1-1-1',
        email='god@example.com',
        password='123456',
    )
    DBSession.add(god)
    DBSession.flush()

    user = User(
        title='alitk',
        first_name='alireza',
        last_name='tavakoli',
        birth_date='1993-4-16',
        email='ali@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='hamiid',
        first_name='hamid',
        last_name='jacob',
        birth_date='1996-9-1',
        email='famil@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='rez',
        first_name='reza',
        last_name='ebrahimi',
        birth_date='1994-4-4',
        email='reza@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='mamad',
        first_name='mohammad',
        last_name='javadi',
        birth_date='1994-7-21',
        email='mamad@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='milawd',
        first_name='milad',
        last_name='ameri',
        birth_date='1994-3-1',
        email='milad@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='behroooz',
        first_name='behrouz',
        last_name='pashaei',
        birth_date='1994-4-4',
        email='behrouz@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='javati',
        first_name='javad',
        last_name='hashemi',
        birth_date='1993-6-25',
        email='javad@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='alifamil',
        first_name='ali',
        last_name='famil',
        birth_date='1996-6-25',
        email='famil@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title='mehranii',
        first_name='mehran',
        last_name='rezvani',
        birth_date='1996-6-25',
        email='famil@example.com',
        password='123456',
    )
    DBSession.add(user)
    DBSession.flush()

    DBSession.commit()

    print('Following user has been added:')
    print(god)

