import datetime

from bddrest import status, response, when, given

from .helpers import LocalApplicationTestCase


class TestUser(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        pass


def test_add(self):
    title = 'Event1'
    repeat = 'never'
    event_type_id = self.event_type_personal.id
    start_date = datetime.datetime.now().isoformat()
    end_date = datetime.datetime.now().isoformat()

    with self.given(
            'Adding an event',
            '/apiv1/users',
            'CREATE',
            json=dict(
                title=title,
                startDate=start_date,
                endDate=end_date,
                repeat=repeat,
                eventTypeId=event_type_id,
                memberId=self.member1.id,
                organizationId=self.organization1.id,
            ),
    ):
        assert status == 200
        assert response.json['id'] is not None
