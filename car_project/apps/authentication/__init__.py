from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'car_project.apps.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import car_project.apps.authentication.signals

#custom app config
default_app_config = 'car_project.apps.authentication.AuthenticationAppConfig'