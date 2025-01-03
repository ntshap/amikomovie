from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: jangan gunakan debug=True di production!
DEBUG = False

# Tambahkan domain Azure Anda ke ALLOWED_HOSTS
ALLOWED_HOSTS = [
    'amikomovie0-ewhkdgchd0eeh0hc.canadacentral-01.azurewebsites.net',
    'localhost',
    '127.0.0.1'
]

# Aplikasi yang terinstall
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'whitenoise.runserver_nostatic',  # Tambahkan whitenoise
]

# Tambahkan Whitenoise middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Tambahkan setelah SecurityMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database dengan timeout settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'amikomovie',
        'USER': 'amikomovie',
        'PASSWORD': 'Cloud_1234',
        'HOST': 'amikomovie.postgres.database.azure.com',
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
            'connect_timeout': 30,
        },
        'CONN_MAX_AGE': 60,
    }
}

# Logging konfigurasi
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'WARNING',
        },
    },
}

# Static files konfigurasi
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Security settings
CSRF_TRUSTED_ORIGINS = [
    'https://amikomovie0-ewhkdgchd0eeh0hc.canadacentral-01.azurewebsites.net',
    'https://django-netflix-clone-dev-tmkz.4.us-1.fl0.io'
]
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Timeout settings
SESSION_COOKIE_AGE = 3600  # 1 jam
SESSION_SAVE_EVERY_REQUEST = True
