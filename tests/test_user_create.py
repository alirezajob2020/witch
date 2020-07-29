import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestUser(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass

    def test_create(self):
        title = 'Event1'
        start_date = datetime.datetime.now().isoformat()
        end_date = datetime.datetime.now().isoformat()

        with self.given(
                'Create an event',
                '/apiv1/users',
                'CREATE',
                json=dict(
                    title=title,
                    startDate=start_date,
                    endDate=end_date,
                ),
        ):

            assert status == 200
