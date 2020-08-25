from restfulpy.orm import DBSession

from witch.models.user import User


def insert():

    user = User(
        title="user1",
        first_name="u1",
        last_name="m1",
        birth_date="1999-5-5",
        email="user1",
        password="qweacsd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user2",
        first_name="u2",
        last_name="m2",
        birth_date="1999-5-5",
        email="user2",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user3",
        first_name="u3",
        last_name="m3",
        birth_date="1999-5-5",
        email="user3",
        password="qweassd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user4",
        first_name="u4",
        last_name="m4",
        birth_date="1999-5-5",
        email="user4",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user5",
        first_name="u5",
        last_name="m5",
        birth_date="1999-5-5",
        email="user5",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user6",
        first_name="u6",
        last_name="m6",
        birth_date="1999-5-5",
        email="user6",
        password="qwea2sd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user7",
        first_name="u7",
        last_name="m7",
        birth_date="1999-5-5",
        email="user7",
        password="qweas1d"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user8",
        first_name="u8",
        last_name="m8",
        birth_date="1999-5-5",
        email="user8",
        password="qwesd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user9",
        first_name="u9",
        last_name="m9",
        birth_date="1999-5-5",
        email="user9",
        password="qeasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user10",
        first_name="u10",
        last_name="m10",
        birth_date="1999-5-5",
        email="user10",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user11",
        first_name="u11",
        last_name="m11",
        birth_date="1999-5-5",
        email="user11",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user12",
        first_name="u12",
        last_name="m12",
        birth_date="1999-5-5",
        email="user12",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user13",
        first_name="u13",
        last_name="m13",
        birth_date="1999-5-5",
        email="user13",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user14",
        first_name="u14",
        last_name="m14",
        birth_date="1999-5-5",
        email="user14",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user15",
        first_name="u15",
        last_name="m15",
        birth_date="1999-5-5",
        email="user15",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user16",
        first_name="u16",
        last_name="m16",
        birth_date="1999-5-5",
        email="user16",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user17",
        first_name="u17",
        last_name="m17",
        birth_date="1999-5-5",
        email="user17",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user18",
        first_name="u18",
        last_name="m18",
        birth_date="1999-5-5",
        email="user18",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user19",
        first_name="u19",
        last_name="m19",
        birth_date="1999-5-5",
        email="user19",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    user = User(
        title="user20",
        first_name="u20",
        last_name="m20",
        birth_date="1999-5-5",
        email="user20",
        password="qweasd"
    )
    DBSession.add(user)
    DBSession.flush()

    DBSession.commit()

