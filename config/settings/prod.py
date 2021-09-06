from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
