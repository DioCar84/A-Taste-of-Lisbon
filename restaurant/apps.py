from django.apps import AppConfig


class RestaurantConfig(AppConfig):
    """
    The RestaurantConfig class defines the django
    configuration for the restaurant app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'restaurant'
