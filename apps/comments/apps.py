from django.apps import AppConfig


class ProductCommentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.comments'

    def ready(self):
        import apps.comments.signals