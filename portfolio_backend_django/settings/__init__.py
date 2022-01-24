from django.conf import settings

from .base import *

if settings.ENV_STAGE == "Production":
    from .production import *
elif settings.ENV_STAGE == "Staging":
    from .staging import *
else:
    from .local import *
