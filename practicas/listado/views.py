from django.shortcuts import render

# Create your views here.

def listado(request):
    return render(request,'listado.html')