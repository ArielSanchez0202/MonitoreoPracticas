from django.urls import path
from . import views
from .views import verificar_practica1

urlpatterns = [
    path('', views.estudiante_view, name='estudiante'),
    path('inscripcion_practica/', views.inscripcion_practica_view, name='inscripcion_practica'),
    path('api/verificar_practica1/', verificar_practica1, name='verificar_practica1'),
]
