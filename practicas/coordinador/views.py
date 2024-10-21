import pandas as pd
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Estudiante
from .forms import EstudianteForm
from django.http import HttpResponse
import openpyxl
from django.core.files.storage import FileSystemStorage

# Create your views here.

def agregar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['correo_electronico']
            rut = form.cleaned_data['rut']
            
            # Verificar si ya existe un usuario con el mismo username (RUT)
            if User.objects.filter(username=rut).exists():
                messages.error(request, "El RUT ya está registrado.")
                return render(request, 'coordinador/agregar_estudiante.html', {'form': form})

            # Crear el usuario usando el modelo User de Django
            usuario = User.objects.create_user(username=rut, email=email, first_name=nombre)
            usuario.set_password('password123')  # Configurar contraseña predeterminada
            usuario.save()

            grupo, _ = Group.objects.get_or_create(name='Estudiantes')
            usuario.groups.add(grupo)

            estudiante = Estudiante(
                usuario=usuario,
                rut=rut,
                domicilio=form.cleaned_data['domicilio'],
                carrera=form.cleaned_data['carrera']
            )
            estudiante.save()

            messages.success(request, "Estudiante agregado exitosamente.")
            return redirect('coordinador:listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'coordinador/agregar_estudiante.html', {'form': form})

def carga_masiva_estudiantes(request):
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if not archivo:
            messages.error(request, "Por favor, selecciona un archivo.")
            return redirect('coordinador:carga_masiva_estudiantes')

        # Procesar el archivo Excel
        try:
            # Leer el archivo Excel
            df = pd.read_excel(archivo, engine='openpyxl')
            # Verificar las primeras filas del DataFrame para depuración
            print("Primeras filas del DataFrame:", df.head())
            # Renombrar las columnas para evitar espacios (solo hay 5 columnas, no 6)
            df.columns = ['Nombre', 'CorreoElectronico', 'RUT', 'Domicilio', 'Carrera']

            # Asegúrate de que el archivo tiene las columnas correctas
            columnas_esperadas = {'Nombre', 'CorreoElectronico', 'RUT', 'Domicilio', 'Carrera'}
            if not columnas_esperadas.issubset(df.columns):
                messages.error(request, "El archivo no tiene las columnas requeridas.")
                return redirect('coordinador:carga_masiva_estudiantes')

            # Convertir el DataFrame a una lista de diccionarios para previsualización
            estudiantes = df.to_dict(orient='records')
            # Guardar los estudiantes procesados en la sesión
            request.session['alumnos_preview'] = estudiantes
            return render(request, 'coordinador/carga_masiva_estudiantes.html', {'estudiantes': estudiantes})
        except Exception as e:
            # Depuración: Mostrar el error en la consola
            print(f"Error al procesar el archivo: {e}")
            messages.error(request, f"Error al procesar el archivo: {e}")
            return redirect('coordinador:carga_masiva_estudiantes')
    return render(request, 'coordinador/carga_masiva_estudiantes.html')
def previsualizar_estudiantes(request):
    alumnos = request.session.get('alumnos_preview', [])
    if request.method == 'POST':
        for alumno in alumnos:
            rut = alumno['RUT']
            email = alumno['CorreoElectronico']
            nombre = alumno['Nombre']
            domicilio = alumno['Domicilio']
            carrera = alumno['Carrera']
            # Verifica si el estudiante ya existe
            if not User.objects.filter(username=rut).exists():
                usuario = User.objects.create_user(username=rut, email=email, first_name=nombre)
                usuario.set_password('password123')
                usuario.save()

                grupo, _ = Group.objects.get_or_create(name='Estudiantes')
                usuario.groups.add(grupo)

                # Crear el estudiante asociado al usuario
                estudiante = Estudiante(
                    usuario=usuario,
                    rut=rut,
                    domicilio=domicilio,
                    carrera=carrera
                )
                estudiante.save()

        # Elimina la sesión temporal de la previsualización
        request.session.pop('alumnos_preview', None)
        messages.success(request, "Estudiantes añadidos exitosamente.")
        return redirect('coordinador:listar_estudiantes')

    return render(request, 'coordinador/carga_masiva_preview.html', {'alumnos': alumnos})

def descargar_plantilla_estudiantes(request):
    columnas = ['Nombre Completo', 'Correo Electrónico', 'RUT', 'Domicilio', 'Carrera']
    df = pd.DataFrame(columns=columnas)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=plantilla_estudiantes.xlsx'
    df.to_excel(response, index=False, engine='openpyxl')
    return response
def listar_estudiantes(request):
    estudiantes = Estudiante.objects.all()  # Obtiene todos los estudiantes
    return render(request, 'coordinador/listar_estudiantes.html', {'estudiantes': estudiantes})