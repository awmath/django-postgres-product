# -*- coding: utf-8 -*-
SECRET_KEY = "fake-key"
INSTALLED_APPS = ["tests", "postgres_product"]

import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "test",
        "USER": "test",
        "PASSWORD": "test",
        "HOST": os.environ.get("DB_HOST", "postgres"),
        "PORT": "5432",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
