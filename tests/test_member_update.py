from bddrest import status, response, when, given

from witch.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member1 = Member(
            title='mma',
            email='qq@msn.com',
            first_name='alirezaa',
            last_name='tavakoli',
            gender='male',
            password='Abc123123',
        )
        session.add(cls.member1)

        cls.member2 = Member(
            title='alitkmm',
            email='alireza@msn.com',
            first_name='alirezaa',
            last_name='tavakoli',
            gender='male',
            password='Abc123123',
        )
        session.add(cls.member2)
        session.commit()

    def test_update(self):
        self.login(email='qq@msn.com', password='Abc123123')

        title = 'wwqweqas'
        first_name = 'alireza'
        last_name = 'tk'
        gender = 'male'
        email = 'alirezaaa@msn.com'

        with self.given(
                'update member',
                f'/apiv1/members/id:{self.member1.id}',
                'UPDATE',
                multipart=dict(
                    title=title,
                    firstName=first_name,
                    lastName=last_name,
                    gender=gender,
                    email=email,
                ),
        ):
            assert status == 200

            when(
                'duplicated title',
                multipart=dict(title='alitkmm')
            )
            assert status == '400 title is already exist'

            when(
                'duplicated email',
                multipart=dict(email='alireza@msn.com')
            )
            assert status == '400 email address is already exist'

            when(
                'Trying to pass less than 3 character',
                multipart=dict(title='aq')
            )
            assert status == '400 Title Length Must Be Greater Than 3 ' \
                             'Characters and Less than 256 Character'

            when(
                'Trying to pass greater than 256 character',
                multipart=dict(title='a' * 258)
            )
            assert status == '400 Title Length Must Be Greater Than 3 ' \
                             'Characters and Less than 256 Character'

            when(
                'Trying to pass invalid email format',
                multipart=dict(email='asd.com')
            )
            assert status == '400 Invalid Email Format'

            when('Request is not authorized', authorization=None)
            assert status == 401

        self.logout()
