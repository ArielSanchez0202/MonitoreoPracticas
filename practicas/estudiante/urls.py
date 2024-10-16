from django.urls import path
from . import views

urlpatterns = [
    path('', views.estudiante_view, name='estudiante'),
    path('inscripcion_practica/', views.inscripcion_practica_view, name='inscripcion_practica'),
]
