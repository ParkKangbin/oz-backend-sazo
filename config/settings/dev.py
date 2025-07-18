from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "sazo_db",
        "USER": "sazo_user",
        "PASSWORD": "1234",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
