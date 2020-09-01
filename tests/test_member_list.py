from bddrest import status, response, when, given

from witch.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        user1 = Member(
            email='alireza@msn.com',
            title='alitk777',
            first_name='alirezaa2',
            last_name='tavakoli1',
            password='ABc123123',
        )
        session.add(user1)

        user2 = Member(
            email='alireza1@msn.com',
            title='alitk778',
            first_name='alizaaaaa',
            last_name='tavakoliiii',
            password='ABc1231234',
        )
        session.add(user2)

        user3 = Member(
            email='alireza2@msn.com',
            title='alitk779',
            first_name='ali',
            last_name='tavakoliiii',
            password='ABc1231232',
        )
        session.add(user3)

        session.commit()

    def test_create(self):
        self.login(email='alireza@msn.com', password='ABc123123')

        with self.given(
                'get users list',
                '/apiv1/members',
                'LIST',
        ):
            assert status == 200
            assert len(response.json) == 3

            when('Request is not authorized', authorization=None)
            assert status == 401

            when('Trying to sorting response', query=dict(sort='id'))
            assert len(response.json) == 3
            index = 1
            while index < len(response.json):
                assert response.json[index - 1]['id'] < \
                   response.json[index]['id']
                index += 1

            when('Sorting the response descending', query=dict(sort='-id'))
            assert len(response.json) == 3
            assert response.json[0]['id'] > response.json[1]['id']
            assert response.json[0]['id'] > response.json[1]['id']

            when('Trying pagination response', query=dict(take=1))
            assert len(response.json) == 1

            when('Trying pagination with skip', query=dict(take=1, skip=1))
            assert len(response.json) == 1

            when('Trying filtering response', query=dict(id=1))
            assert response.json[0]['id'] == 1
            assert len(response.json) == 1

            when('Request is not authorized', authorization=None)
            assert status == 401

        self.logout()
