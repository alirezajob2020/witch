from witch.models.member import Member
from tests.helpers import LocalApplicationTestCase


class TestDatabaseCLI(LocalApplicationTestCase):

    def test_basedata(self):
        self.__application__.insert_mockup()
        session = self.create_session()

        assert session.query(Member).count() == 10

