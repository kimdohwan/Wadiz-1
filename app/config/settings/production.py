from .base import *
# secrets = json.loads(open(os.path.join(SECRETS_DIR, 'dev.json')).read())
secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DEBUG = False

ALLOWED_HOSTS = secrets['ALLOWED_HOSTS']
# WSGI
WSGI_APPLICATION = 'config.wsgi.production.application'

# DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Static
STATIC_URL = '/static/'

LOG_DIR = '/var/log/django'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            'format': '[%(asctime)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file_error': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'django.server',
            'backupCount': 10,
            'filename': os.path.join(LOG_DIR, 'error.log'),
            'maxBytes': 10485760,
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file_error'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}