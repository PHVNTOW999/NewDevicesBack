from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-1fa1rtj39pv%jy6%2l5^+ifzq@mfe0m0@@sr2obgmiuwfd*qc*'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '127.0.0.1:8000',
    'http://localhost',
    'http://localhost:3000',
    '195.80.238.204',
    '195.80.238.204:4000',
]

CORS_ORIGIN_WHITELIST = [
    '127.0.0.1',
    '127.0.0.1:8000',
    'http://localhost',
    'http://localhost:3000',
    '195.80.238.204',
    '195.80.238.204:4000',
]

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1',
    'http://127.0.0.1:8000',
    'http://localhost',
    'http://localhost:3000',
    'http://195.80.238.204',
    'http://195.80.238.204:4000',
]


CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'info',
    'finance',
    'reports',
    'corsheaders',
]

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'app.wsgi.application'

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True

# CORS_REPLACE_HTTPS_REFERER = False
HOST_SCHEME = "http://"
# SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = False
# SESSION_COOKIE_SECURE = False
# CSRF_COOKIE_SECURE = False
# SECURE_HSTS_SECONDS = None
# SECURE_HSTS_INCLUDE_SUBDOMAINS = False
# SECURE_FRAME_DENY = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATETIME_INPUT_FORMATS = "%m/%d/%Y %H:%M"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Yerevan'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
