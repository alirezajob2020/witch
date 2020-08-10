from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestToken(LocalApplicationTestCase):

    def test_create(self):
        email = 'ali@gmail.com'
        password = 'Alitk123123'

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
