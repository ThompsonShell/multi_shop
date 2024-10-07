from django.apps import AppConfig


class AboutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.abouts'

    def ready(self):
        import apps.abouts.signals
