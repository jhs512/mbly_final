"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i8=%32qj0rdq9@oy_41+c&!o(oea54jl7b_)f7^3sp=u)s@4#='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    # 서드파티
    'django_bootstrap5',
    'django_pydenticon',
    "rest_framework",
    "corsheaders",
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'django_summernote',
    'django_extensions',
    # 로컬
    'db_var.apps.DbVarConfig',
    'tags.apps.TagsConfig',
    'summernote_support.apps.SummernoteSupportConfig',
    'accounts.apps.AccountsConfig',
    'qna.apps.QnaConfig',
    'markets.apps.MarketsConfig',
    'products.apps.ProductsConfig',
    'cart.apps.CartConfig',
    'seed.apps.SeedConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'base/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_settings_export.settings_export',  # TODO 3주차 설명, django-settings-export 사용설정, 굉장히 좋습니다.
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sample1_dev',
        'USER': 'sbsst',
        'PASSWORD': 'sbs123414',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 추가
AUTH_USER_MODEL = 'accounts.User'

# 장고 디버그툴바 때문에 추가함, 딱히 안해도 되지만, 디버그툴바가 외부에서 쓰이지 않게 해줍니다.
INTERNAL_IPS = [
    "127.0.0.1",
]

STATICFILES_DIRS = [
    BASE_DIR / 'base/static',
]

# 개발자가 구성한 정적파일들의 폴더 경로
STATIC_ROOT = BASE_DIR / 'static'

# 사용자가 업로드한 정적파일폴더 경로
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# TODO 3주차 설명, 이거 안하면 외부에서 이 서버의 API를 사용하지 못합니다.
CORS_ALLOW_CREDENTIALS = True

# 실제 운영서버 도메인
# 장고 최신버전부터 이걸 안하면 안됨
CSRF_TRUSTED_ORIGINS = ['https://sample1.public.473.be', 'https://site7.public.473.be', 'https://cdpn.io']

# TODO 3주차 설명, 이거 안하면 외부에서 이 서버의 API를 사용하지 못합니다.
CORS_ORIGIN_WHITELIST = CSRF_TRUSTED_ORIGINS

# DRF

# TODO 3주차 설명, 이본 인증 클래스에 꼭 SessionAuthentication 을 넣어주세요. 편합니다.
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTTokenUserAuthentication',  # rest_framework_simplejwt.authentication.JWTAuthentication 사용하지 마세요.
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100
}

# TODO 3주차 설명, 엑세스키와 리프레시키의 수명 설정
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=60 * 10),  # 이 부분과
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=60 * 60 * 24 * 30),  # 이 부분만 고치면 됩니다.
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

SITE_NAME = "멋블리!!!"

SETTINGS_EXPORT = [
    'SITE_NAME',
]

# Email with Send Grid
# https://myaccount.google.com/apppasswords 에서 발급
GMAIL_EMAIL_API_KEY = os.environ.get("GMAIL_EMAIL_API_KEY")
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'jangka512@gmail.com'
EMAIL_HOST_PASSWORD = GMAIL_EMAIL_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True

WELCOME_EMAIL_SENDER = EMAIL_HOST_USER

SUMMERNOTE_CONFIG = {
    'summernote': {
        'width': '100%',
        'lang' : 'ko-KR',
    }
}

ELASTIC_HOST = os.environ.get("ELASTIC_HOST", "http://192.168.56.102:9200")
ELASTIC_ID = os.environ.get('ELASTIC_ID', 'elastic')
ELASTIC_PW = os.environ.get('ELASTIC_PW', 'elasticpassword')

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}

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
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/common.log',
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'app': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}
