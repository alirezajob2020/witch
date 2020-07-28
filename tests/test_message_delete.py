import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestMessage(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass

    def test_delete(self):
        title = 'Message1'
        repeat = 'never'
        start_date = datetime.datetime.now().isoformat()
        end_date = datetime.datetime.now().isoformat()

        with self.given(
                'Delete a message',
                '/apiv1/messages',
                'DELETE',
                json=dict(
                    title=title,
                    startDate=start_date,
                    endDate=end_date,
                    repeat=repeat,
                ),
        ):

            assert status == 200
