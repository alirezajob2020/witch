from bddrest import status, response, when, given

from witch.models.user import User
from tests.helpers import LocalApplicationTestCase


class TestToken(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        user = User(
            email='alireza@msn.com',
            title='alitk777',
            first_name='alirezaa',
            last_name='tavakoli',
            password='ABc123123',
        )
        session = cls.create_session()
        session.add(user)
        session.commit()

    def test_create(self):
        email = 'alireza@msn.com'
        password = 'ABc123123'

        with self.given(
                'get token',
                '/apiv1/tokens',
                'CREATE',
                json=dict(
                    email=email,
                    password=password,
                ),
        ):
            assert status == 200
            assert 'token' in response.json

            when('Invalid password', json=given | dict(password='Ss1236'))
            assert status == '400 Incorrect Email Or Password'

            when('Not exist email',
                 json=given | dict(email='user@example.com'))
            assert status == '400 Incorrect Email Or Password'

            when('Invalid email format', json=given | dict(email='user.com'))
            assert status == '400 Invalid Email Format'

            when('Trying to pass with empty form', json={})
            assert status == '400 Empty Form'
