from .base import *
from decouple import config


if config("ENV_STAGE") == 'Production':
    from .production import *
elif config("ENV_STAGE") == 'Staging':
    from .staging import *
else:
    from .local import *
