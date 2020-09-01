
from nanohttp import validate, HTTPStatus, context, int_or_notfound, \
    HTTPBadRequest
from restfulpy.datetimehelpers import parse_datetime
from restfulpy.orm import DBSession

from .exceptions import *
from .models import member

# TITLE_PATTERN = re.compile(r'^(?!\s).*[^\s]$')
# DATETIME_PATTERN = re.compile(
#     r'^(\d{4})-(0[1-9]|1[012]|[1-9])-(0[1-9]|[12]\d{1}|3[01]|[1-9])' \
#     r'(T(2[0-3]|[01][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z)?)?$'
# )
# ORGANIZATION_TITLE_PATTERN = re.compile(
#     r'^([0-9a-zA-Z]+-?[0-9a-zA-Z]*)*[\da-zA-Z]$'
# )
#
# WORKFLOW_TITLE_PATTERN = re.compile(r'^[^\s].+[^\s]$')
