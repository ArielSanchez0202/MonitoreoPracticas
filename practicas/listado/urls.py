from django.urls import path
from . import views

urlpatterns = [
    path('', views.listado_practicas, name='listado_practicas'),
]