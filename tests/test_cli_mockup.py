from witch.models.user import User
from tests.helpers import LocalApplicationTestCase


class TestDatabaseCLI(LocalApplicationTestCase):

    def test_mockup(self):
        self.__application__.insert_mockup()
        session = self.create_session()

        assert session.query(User).count() == 20
