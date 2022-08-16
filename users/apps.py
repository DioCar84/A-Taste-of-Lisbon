from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    The UsersConfig class defines the django configuration for the users app.
    Also allows the use of signals by importing them.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals
