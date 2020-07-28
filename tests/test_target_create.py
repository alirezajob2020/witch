import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestTarget(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass

    def test_create(self):
        title = 'target1'
        repeat = 'never'
        start_date = datetime.datetime.now().isoformat()
        end_date = datetime.datetime.now().isoformat()

        with self.given(
                'Create a target',
                '/apiv1/targets',
                'CREATE',
                json=dict(
                    title=title,
                    startDate=start_date,
                    endDate=end_date,
                    repeat=repeat,
                ),
        ):

            assert status == 200
