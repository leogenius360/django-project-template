

import os
import dj_database_url
from pathlib import Path


from .env_setup import config           # Project Config settings
from .project_settings import (
    PROJECT_APPS
)                                       # Project related settings
from .third_party_settings import (
    THIRD_PARTY_APPS
)     # Third Party related settings


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = config.SECRET_KEY
DEBUG = config.DEBUG
# DEBUG_TEMPLATES = config.DEBUG_TEMPLATES
USE_SSL = config.USE_SSL
ALLOWED_HOSTS = config.ALLOWED_HOSTS

if not USE_SSL:
    SECURE_PROXY_SSL_HEADER = None
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_HSTS_INCLUDE_SUBDOMAINS = False
    SECURE_HSTS_PRELOAD = False
else:
    # IMPORTANT: ONLY APPLY THESE ON THE SERVER !
    #
    # (security.W008) Your SECURE_SSL_REDIRECT setting is not set to True. Unless your
    #                 site should be available over both SSL and non-SSL connections, you
    #                 may want to either set this setting True or configure a load balancer
    #                 or reverse-proxy server to redirect all connections to HTTPS.
    # https://help.heroku.com/J2R1S4T8/can-heroku-force-an-application-to-use-ssl-tls
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SECURE_SSL_REDIRECT = True

    # (security.W012) SESSION_COOKIE_SECURE is not set to True. Using a secure-only session
    #                 cookie makes it more difficult for network traffic sniffers to hijack
    #                 user sessions.
    SESSION_COOKIE_SECURE = True

    # (security.W016) You have 'django.middleware.csrf.CsrfViewMiddleware' in your
    #                 MIDDLEWARE, but you have not set CSRF_COOKIE_SECURE to True. Using a
    #                 secure-only CSRF cookie makes it more difficult for network traffic
    #                 sniffers to steal the CSRF token.
    CSRF_COOKIE_SECURE = True

    # IMPORTANT:
    # (-) Add these only once the HTTPS redirect is confirmed to work
    #
    # (security.W004) You have not set a value for the SECURE_HSTS_SECONDS setting. If your
    #                 entire site is served only over SSL, you may want to consider setting
    #                 a value and enabling HTTP Strict Transport Security. Be sure to read
    #                 the documentation first; enabling HSTS carelessly can cause serious,
    #                 irreversible problems.
    SECURE_HSTS_SECONDS = 2592000  # 1 month
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]



INSTALLED_APPS = DEFAULT_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


os.environ["DATABASE_URL"] = config.DATABASE_URL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },

    "psql": dj_database_url.config(conn_max_age=600, ssl_require=config.DATABASE_SSL)
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = 'media/'
MEDIA_DIRS = (os.path.join(BASE_DIR, 'media/'),)
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

