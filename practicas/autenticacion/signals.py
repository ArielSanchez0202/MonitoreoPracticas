# autenticacion/signals.py
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group

@receiver(post_migrate)
def create_user_groups(sender, **kwargs):
    if sender.name == 'autenticacion':  # Verifica que la señal sea de tu aplicación
        Group.objects.get_or_create(name='Estudiante')
        Group.objects.get_or_create(name='Coordinador')
