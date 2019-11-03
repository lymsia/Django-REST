import os

from .setting_common import *

ENVIRONMENT = os.environ.get('ENVIRONMENT')

if ENVIRONMENT == 'dev':
    from .setting_dev import *
else:
    from .setting_prod import *
