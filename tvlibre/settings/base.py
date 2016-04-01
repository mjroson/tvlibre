import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = '^os4$rdo-ieb!-o&)gh8tv663h@*omj0flua3ruk=y8w5f8x2w'


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',

    'allauth', # manager authentication support for social network
    'allauth.account',
    'allauth.socialaccount',

    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.twitter',

    'admin_shortcuts', # Add shortcut or menu on django admin index.
    'flat', # theme flat on django admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    'bootstrap3', # print form to support bootstrap with templatetag
    'django_comments',
    'django_comments_xtd', # comment
    'djmail', # send async email
    'embed_video', # embed video on admin
    #'haystack',
    'jsonify', # cast json in template
    'rest_framework', # make api rest full
    'sorl.thumbnail',
    'taggit',

    # My packages
    'apps.comments',
    'apps.favorite',
    'apps.program',
    'apps.notification',
    'apps.user',
    'apps.userProfile',
)



MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'tvlibre.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'tvlibre.wsgi.application'


LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), "static")



STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = "/media/"


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ),
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.AdminRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ],
    'DEFAULT_PAGINATION_CLASS': 'tvlibre.views.CustomPagination',
    'PAGE_SIZE': 6
}

EMBED_VIDEO_BACKENDS = (
    'embed_video.backends.YoutubeBackend',
    'embed_video.backends.VimeoBackend',
    'embed_video.backends.SoundCloudBackend',
    #'my_app.backends.CustomBackend',
)

TAGGIT_CASE_INSENSITIVE = True

SITE_ID = 1



#### DJANGO ALLAUTH CONFIG #######
#SOCIALACCOUNT_ENABLED = True

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)


LOGIN_URL = '/cuenta/entrar/'
LOGIN_REDIRECT_URL = '/'
ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS = '/'

ACCOUNT_AUTHENTICATION_METHOD = 'username_email'

ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https'

ACCOUNT_ADAPTER = "apps.user.adapter.CustomAccountAdapter"

# SOCIALACCOUNT_PROVIDERS = {
#     'facebook': {
#         'SCOPE': ['email', 'public_profile'],
#         'METHOD': 'oauth2',
#     },
#     'google': {
#         'SCOPE': ['https://www.googleapis.com/auth/userinfo.profile'],
#         'AUTH_PARAMS': {'access_type': 'online'}
#
#     }
# }

#SOCIALACCOUNT_EMAIL_VERIFICATION=True

COMMENTS_APP = "django_comments_xtd"
COMMENTS_XTD_CONFIRM_EMAIL = True
COMMENTS_XTD_MAX_THREAD_LEVEL = 2



ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
                },
            {
                'url_name': 'admin:program_program_changelist',
                'title': 'Programas',
                'class': 'picture'
                },
            {
                'url_name': 'admin:program_episode_changelist',
                'title': 'Episodios',
                'class': 'film'
                }
        ]
    },
]


###### EMAIL CONFIG

DEFAULT_FROM_EMAIL = 'EMAIL'

EMAIL_BACKEND="djmail.backends.async.EmailBackend"
DJMAIL_REAL_BACKEND="django.core.mail.backends.smtp.EmailBackend"

# Config email
EMAIL_HOST = 'HOST' # Ejemplo: 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_USE_TLS = True

#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_EMAIL_VERIFICATION = True


# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
#     },
# }