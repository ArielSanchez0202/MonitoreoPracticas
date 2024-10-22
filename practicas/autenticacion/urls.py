# autenticacion/urls.py
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('coordinador/', include('coordinador.urls')),
    path('estudiante/', include('estudiante.urls')),
    
]
