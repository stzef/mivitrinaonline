#from config.db import DATABASES as dbconfig
#from config.credentials import CREDENTIALS
import os
import dj_database_url


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
	'storages',
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

AWS_STORAGE_BUCKET_NAME = os.getenv("MVO_AWS_STORAGE_BUCKET_NAME","")
print AWS_STORAGE_BUCKET_NAME
AWS_ACCESS_KEY_ID = os.getenv("MVO_AWS_ACCESS_KEY_ID","")
print AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = os.getenv("MVO_AWS_SECRET_ACCESS_KEY","")
print AWS_SECRET_ACCESS_KEY

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# This is used by the `static` template tag from `static`, if you're using that. Or if anything else
# refers directly to STATIC_URL. So it's safest to always set it.
#STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN

# Tell the staticfiles app to use S3Boto storage when writing the collected static files (when
# you run `collectstatic`).
#STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

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

if "DATABASE_URL" in os.environ:
	#DATABASES = dbconfig
	DATABASES = {
		'default' : dj_database_url.parse(os.environ.get("DATABASE_URL"), conn_max_age=600)
	}

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

LOGIN_URL = '/ingresar'

LOGOUT_URL = '/salir'

STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#MEDIA_URL = '/media/'
