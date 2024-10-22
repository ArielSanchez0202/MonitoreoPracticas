# autenticacion/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from autenticacion.forms import LoginForm
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)  # Usa tu formulario aquí
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirección basada en el rol
                if user.groups.filter(name='Coordinador').exists():
                    return redirect('coordinador:listar_estudiantes')  # Ajusta el nombre de la URL
                elif user.groups.filter(name='Estudiante').exists():
                    return redirect('inscripcion_practica')  # Ajusta el nombre de la URL
                else:
                    return redirect('home')  # Redirección por defecto
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales inválidas'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Credenciales inválidas'})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Asegúrate de que la URL de login esté definida en tu app
