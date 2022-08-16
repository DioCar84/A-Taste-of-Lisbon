from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    The BlogConfig class defines the django configuration for the blog app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
