import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'account',
)

SECRET_KEY = '6few3nci_q_o@l1dlbk81%wcxe!*6r29yu629&d97!hiqat9fa'
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True
