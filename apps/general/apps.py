from django.apps import AppConfig


class GeneralsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.general'

def ready():
    import apps.general.signals
