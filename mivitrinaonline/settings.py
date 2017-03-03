from config.db import DATABASES as dbconfig
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = "ia=1dinj8#(uo!_hdzf6jh3_==w99!3r98m=6$8z=7n7%%h79^"

DEBUG = True

TEMPLATE_DEBUG = True

DJANGO_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.messages',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'django.contrib.humanize',
)

PROJECT_APPS = (
	'app',
	'busquedas',
	'estadisticas',
	'bienes_servicios',
	'usuarios',
)

THIRTY_PARTY_APPS = (
	'djrill',
)

#https://mvostorage.blob.core.windows.net/mvofiles
#http://azure_account_name.blob.core.windows.net/

DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
AZURE_ACCOUNT_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
AZURE_ACCOUNT_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
AZURE_CONTAINER = os.environ.get("AZURE_CONTAINER")

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRTY_PARTY_APPS

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# SMTP Settings Backend
EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

MANDRILL_API_KEY = 'jxuFDPFiFErIiMd0c-cbXw'

DEFAULT_FROM_EMAIL = "sistematizaref@gmail.com"
# SMTP Settings Backend




ROOT_URLCONF = 'mivitrinaonline.urls'

WSGI_APPLICATION = 'mivitrinaonline.wsgi.application'

LANGUAGE_CODE = 'es-CO'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

if dbconfig:
	DATABASES = dbconfig
	print "Si"
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': 'dbsqlite',
		}
	}
	print "No"

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

"""LOGIN_URL = '/ingresar'
LOGOUT_URL = '/salir'
#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_URL = '/static/'
STATIC_URL = '/static/'
#STATICFILES_DIRS = (
	#os.path.join(BASE_DIR, 'static'),
#)
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'"""

LOGIN_URL = '/ingresar'

LOGOUT_URL = '/salir'

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'