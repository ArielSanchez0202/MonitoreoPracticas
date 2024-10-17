from django.shortcuts import render

def estudiante_view(request):
    return render(request, 'estudiante.html')

def inscripcion_practica_view(request):
    return render(request, 'inscripcion_practica.html')
