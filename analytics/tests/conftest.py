from django.conf import settings
import pytest
from cs_analytics import db


@pytest.fixture(scope='session')
def django_db_setup():
    settings.DATABASES['default'] = {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dev_csgo_analysis',  # dev db
        'USER': 'postgres',
        'PASSWORD': db.pwd,
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }