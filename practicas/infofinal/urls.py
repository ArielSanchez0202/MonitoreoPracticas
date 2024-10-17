from django.urls import path
from . import views

urlpatterns = [
    path('', views.infofinal, name='infofinal'),
]