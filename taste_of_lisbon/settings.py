from pathlib import Path
import os
from django.contrib.messages import constants as messages
import dj_database_url

if os.path.isfile('env.py'):
    import env


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')



SECRET_KEY = os.environ.get('SECRET_KEY')


DEBUG = False

ALLOWED_HOSTS = ['a-taste-of-lisbon.herokuapp.com', 'localhost']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'crispy_forms',
    'crispy_bootstrap5',
    'django_summernote',
    'django_extensions',
    'blog.apps.BlogConfig',
    'restaurant.apps.RestaurantConfig',
    'users.apps.UsersConfig'
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'taste_of_lisbon.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'taste_of_lisbon.wsgi.application'



DATABASES = {
    'default':
    dj_database_url.parse(os.environ.get('DATABASE_URL'))
}



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.'
        'password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True

DATE_INPUT_FORMATS = ['%m/%d/%Y']



LOGIN_REDIRECT_URL = 'profile'
LOGIN_URL = 'login'

STATIC_URL = '/static/'

STATICFILES_STORAGE = \
    'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}
