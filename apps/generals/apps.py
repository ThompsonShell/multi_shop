from django.apps import AppConfig


class GeneralsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.generals'

def ready():
    import signals
