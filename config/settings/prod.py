from .base import *

DEBUG = False
ALLOWED_HOSTS = ["yourdomain.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "prod_db",
        "USER": "prod_user",
        "PASSWORD": "prod_pw",
        "HOST": "prod-db-host",
        "PORT": "5432",
    }
}
