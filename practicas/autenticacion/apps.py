# autenticacion/apps.py
from django.apps import AppConfig

class AutenticacionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'autenticacion'

    def ready(self):
        import autenticacion.signals  # Conecta la señal