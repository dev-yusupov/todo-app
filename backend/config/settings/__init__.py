ENV_NAME = 'Local'

from .base import *
import os


if ENV_NAME == 'Production':
    from .production import *
else:
    from .local import *