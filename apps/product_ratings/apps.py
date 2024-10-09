from django.apps import AppConfig


class ProductRatingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.product_ratings'

    def ready(self):
        import apps.product_ratings.signal
