from .base import *

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # This is my general context processors
                'apps.general.context_processors.general_context',
                # This is my wishlist context processors
                'apps.wishlist.context_processors.wishlist_context',
                # This is my category context processors
                'apps.categories.context_processors.categories',

            ],
        },
    },
]
