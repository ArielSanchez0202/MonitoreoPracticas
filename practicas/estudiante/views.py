from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import InscripcionPractica  # Asegúrate de que este modelo esté definido

def estudiante_view(request):
    return render(request, 'estudiante.html')

def inscripcion_practica_view(request):
    return render(request, 'inscripcion_practica.html')

def inscripcion_practica_view(request):
    if request.method == 'POST':
        # Recuperar los datos enviados por el formulario
        nombre_completo = request.POST.get('nombre_completo')
        rut = request.POST.get('rut')
        domicilio = request.POST.get('domicilio')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        carrera = request.POST.get('carrera')
        practica1 = request.POST.get('practica1') == 'on'  # checkbox
        practica2 = request.POST.get('practica2') == 'on'  # checkbox
        razon_social = request.POST.get('razon_social')
        direccion_empresa = request.POST.get('direccion_empresa')
        jefe_directo = request.POST.get('jefe_directo')
        cargo = request.POST.get('cargo')
        telefono_jefe = request.POST.get('telefono_jefe')
        correo_jefe = request.POST.get('correo_jefe')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_termino = request.POST.get('fecha_termino')
        horario_trabajo = request.POST.get('horario_trabajo')
        horario_colacion = request.POST.get('horario_colacion')
        cargo_desarrollar = request.POST.get('cargo_desarrollar')
        depto_trabajar = request.POST.get('depto_trabajar')
        actividades_realizar = request.POST.get('actividades_realizar')

        # Crear una nueva instancia del modelo InscripcionPractica
        inscripcion = InscripcionPractica(
            nombre_completo=nombre_completo,
            rut=rut,
            domicilio=domicilio,
            telefono=telefono,
            correo=correo,
            carrera=carrera,
            practica1=practica1,
            practica2=practica2,
            razon_social=razon_social,
            direccion_empresa=direccion_empresa,
            jefe_directo=jefe_directo,
            cargo=cargo,
            telefono_jefe=telefono_jefe,
            correo_jefe=correo_jefe,
            fecha_inicio=fecha_inicio,
            fecha_termino=fecha_termino,
            horario_trabajo=horario_trabajo,
            horario_colacion=horario_colacion,
            cargo_desarrollar=cargo_desarrollar,
            depto_trabajar=depto_trabajar,
            actividades_realizar=actividades_realizar
        )

        # Guardar la inscripción en la base de datos
        inscripcion.save()

        # Redirigir a estudiante.html después de enviar el formulario exitosamente
        return redirect('estudiante')

    return render(request, 'inscripcion_practica.html')