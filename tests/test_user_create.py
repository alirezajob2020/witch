import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestUser(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass

    def test_create(self):
        name = 'alireza'
        family = 'tavakoli'
        email = 'alitk@msn.com'

        with self.given(
                'Create an event',
                '/apiv1/users',
                'CREATE',
                json=dict(
                    name=name,
                    family=family,
                    email=email,
                ),
        ):
            assert status == 200
