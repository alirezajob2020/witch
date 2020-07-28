import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestUser(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass

    def test_delete(self):
        title = 'Event1'
        repeat = 'never'
        start_date = datetime.datetime.now().isoformat()
        end_date = datetime.datetime.now().isoformat()

        with self.given(
                'Delete an event',
                '/apiv1/users',
                'DELETE',
                json=dict(
                    title=title,
                    startDate=start_date,
                    endDate=end_date,
                    repeat=repeat,
                ),
        ):

            assert status == 200
