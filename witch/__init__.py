from os.path import dirname, join
import functools

from nanohttp import settings
from restfulpy import Application
from sqlalchemy_media import StoreManager, FileSystemStore

from . import mockup
from .authentication import Authenticator
from .controllers.root import Root

__version__ = '0.1'


class Witch(Application):
    __authenticator__ = Authenticator()
    __configuration__ = '''
      db:
        url: postgresql://postgres:postgres@localhost/witch_dev
        test_url: postgresql://postgres:postgres@localhost/witch_test
        administrative_url: postgresql://postgres:postgres@localhost/postgres

      migration:
        directory: %(root_path)s/migration
        ini: %(root_path)s/alembic.ini

      issue:
        subscription:
          max_length: 100

      logging:
        loggers:
          backends:
            propagate: false
            level: debug
            handlers:
              - backend_handler

        handlers:
          backend_handler:
            type: file
            filename: /tmp/witch-backends.log

      oauth:
        secret: A1dFVpz4w/qyym+HeXKWYmm6Ocj4X5ZNv1JQ7kgHBEk=\n
        application_id: 1
        url: http://localhost:8083

      chat:
        url: http://localhost:8084

      organization_invitation:
        secret: !!binary xxSN/uarj5SpcEphAHhmsab8Ql2Og/2IcieNfQ3PysI=
        max_age: 86400  # seconds
        algorithm: HS256
        signin_callback_url: http://localhost:8082/login
        signup_callback_url: http://localhost:8082/register
        signin_template: organization_invitation_email_with_account.mako
        signup_template: organization_invitation_email_without_account.mako

      messaging:
        default_messenger: restfulpy.messaging.ConsoleMessenger
        template_dirs:
          - %(root_path)s/email_templates

      storage:
        local_directory: %(root_path)s/../data/assets
        base_url: http://localhost:8081/assets

      attachments:
        files:
          max_length: 50 # KB
          min_length: 1  # KB
        organizations:
          logos:
            max_length: 50 # KB
            min_length: 1  # KB

      resource:
        load_thresholds:
          heavy: 5
          medium: 3

      weekend: 4 # Friday based on Python week days number

      room:
        subscription:
          max_length: 100

   '''

    def __init__(self, application_name='witch', root=Root()):
        super().__init__(
            application_name,
            root=root,
            root_path=dirname(__file__),
            version=__version__
        )

    def insert_mockup(self, *args):  # pragma: no cover
        mockup.insert()

    @classmethod
    def initialize_orm(cls, engine=None):
        StoreManager.register(
            'fs',
            functools.partial(
                FileSystemStore,
                settings.storage.local_directory,
                base_url=settings.storage.base_url,
            ),
            default=True
        )
        super().initialize_orm(cls, engine)


witch = Witch()
