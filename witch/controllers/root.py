from os.path import abspath, dirname, join

from nanohttp import json, Static
from restfulpy.controllers import RootController, RestController, \
    JSONPatchControllerMixin

import witch
from .user import UserController
from .token import TokenController

here = abspath(dirname(__file__))
attachment_storage = abspath(join(here, '../..', 'data/assets'))


class Apiv1(RestController, JSONPatchControllerMixin):
    users = UserController()
    tokens = TokenController()

    @json
    def version(self):
        return dict(version=witch.__version__)


class Root(RootController):
    apiv1 = Apiv1()
    assets = Static(attachment_storage)
