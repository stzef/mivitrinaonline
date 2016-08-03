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

#DATABASES = {
#	'default': {
#		'ENGINE': 'django.db.backends.postgresql_psycopg2',
#		'NAME': 'da6sp8fv4gmdmq',
#		'USER': 'kpmzagniuviqmk',
#		'PASSWORD': 'lwU3nDRM25wik5-ItShIWmHThd',
#		'HOST':'ec2-54-243-210-223.compute-1.amazonaws.com',
#		'PORT':'5432',
#	}
#}

if 'RDS_DB_NAME' in os.environ:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': os.environ['RDS_DB_NAME'],
			'USER': os.environ['RDS_USERNAME'],
			'PASSWORD': os.environ['RDS_PASSWORD'],
			'HOST': os.environ['RDS_HOSTNAME'],
			'PORT': os.environ['RDS_PORT'],
		}
	}
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'iotd',
			'USER': 'iotd',
			'PASSWORD': 'iotd',
			'HOST': 'localhost',
			'PORT': '5432',
		}
	}


#DATABASES['default'] =  dj_database_url.config()

# Enable Connection Pooling (if desired)
#DATABASES['default']['ENGINE'] = 'django_postgrespool'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

LOGIN_URL = '/ingresar'

LOGOUT_URL = '/salir'

#STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATIC_URL = '/static/'
STATIC_URL = '/static/'

#STATICFILES_DIRS = (
	#os.path.join(BASE_DIR, 'static'),
#)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'
