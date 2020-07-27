from contextlib import contextmanager
from os import path

from auditor import MiddleWare
from nanohttp import RegexRouteController, json, settings, context, HTTPStatus
from restfulpy.application import Application
from restfulpy.orm.metadata import FieldInfo
from restfulpy.testing import ApplicableTestCase, db

# from .mockup import mockup_http_server
from witch import Witch

HERE = path.abspath(path.dirname(__file__))
DATA_DIRECTORY = path.abspath(path.join(HERE, '../data'))


def callback(audit_logs):
    pass


class LocalApplicationTestCase(ApplicableTestCase):
    __application__ = Witch
    __story_directory__ = path.join(DATA_DIRECTORY, 'stories')
    __api_documentation_directory__ = path.join(DATA_DIRECTORY, 'markdown')

    __configuration__ = '''
            issue:
              subscription:
                max_length: 5
        '''

    def login(self, email, organization_id=None):
        pass