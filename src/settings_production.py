from settings import PPATH
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.mysql',
       'NAME':   'prototypeur',
       'USER': 'manager',
       'PASSWORD': 'password',
       'HOST': 'localhost',
       'PORT': '3306',
   }
}

ALLOWED_HOSTS = [
    'styx', # Allow domain and subdomains
    '127.0.1.1',
]

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.request",
                               "django.contrib.messages.context_processors.messages"
                               )

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # If you want to disable CSRF validation, uncomment the line below and comment the line 'django.middleware.csrf.CsrfViewMiddleware',
    #'prototype.disable.DisableCSRF',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    PPATH + '/templates',

    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.admindocs',
#     'south',
    'protoLib',
    'prototype',
    'll',
)

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'protoext@gmail.com'
DEFAULT_FROM_EMAIL = 'protoext@gmail.com'
with open('/etc/email_key.txt') as f:
    EMAIL_HOST_PASSWORD = f.read().strip()
