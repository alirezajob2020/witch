from bddrest import status, response, when, given

from tests.helpers import LocalApplicationTestCase


class TestUser(LocalApplicationTestCase):

    def test_create(self):
        name = 'alireza'
        fullname = 'tavakoli'
        email = 'alitk@msn.com'

        with self.given(
                'Create a user',
                '/apiv1/users',
                'CREATE',
                json=dict(
                    name=name,
                    fullname=fullname,
                    email=email,
                ),
        ):
            assert status == 200
            assert response.json['id'] is not None
            assert response.json['name'] == name
            assert response.json['fullname'] == fullname
            assert response.json['email'] == email
