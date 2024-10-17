from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listado/',include('listado.urls')),
    path('solicitudes/',include('solicitudes.urls')),
    path('informes/',include('informes.urls')),
    path('autoevaluaciones/',include('autoevaluaciones.urls')),
    path('documentos/',include('documentos.urls')),
    path('infofinal/',include('infofinal.urls')),
    path('salir' ,views.salir, name='salir'),
    path('perfil', views.perfil,name='perfil'),
]