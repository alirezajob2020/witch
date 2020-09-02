from bddrest import status, response, when, given

from witch.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestMember(LocalApplicationTestCase):

    @classmethod
    def mockup(cls):
        session = cls.create_session()

        cls.member1 = Member(
            title='mma',
            email='qq@msn.com',
            first_name='alirezaa',
            last_name='tavakoli',
            password='Abc123123',
        )
        session.add(cls.member1)

        cls.member2 = Member(
            title='alitkmm',
            email='alireza@msn.com',
            first_name='alirezaa',
            last_name='tavakoli',
            password='Abc123123',
        )
        session.add(cls.member2)
        session.commit()

    def test_update(self):
        self.login(email='qq@msn.com', password='Abc123123')

        with self.given(
                'delete member',
                f'/apiv1/members/id: {self.member1.id}',
                'DELETE',
        ):
            assert status == 200
            assert response.json['id'] == self.member1.id
            assert response.json['title'] == self.member1.title
            assert response.json['email'] == self.member1.email
            assert response.json['firstName'] == self.member1.first_name
            assert response.json['lastName'] == self.member1.last_name

            session = self.create_session()
            assert not session.query(Member) \
                .filter(Member.id == self.member1.id) \
                .one_or_none()

            when('Request is not authorized', authorization=None)
            assert status == 401

        self.logout()
