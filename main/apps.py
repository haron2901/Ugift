from django.apps import AppConfig


class MainConfig(AppConfig):
    dlt_auto_field = 'django.db.models.BigAutoField'
    name = 'main'