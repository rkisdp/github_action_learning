from .base import *
from django.conf import settings


if settings.ENV_STAGE == 'Production':
    from .production import *
elif settings.ENV_STAGE == 'Staging':
    from .staging import *
else:
    from .local import *
