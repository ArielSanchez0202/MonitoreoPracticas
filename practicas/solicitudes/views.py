from django.shortcuts import render

# Create your views here.
def solicitudes(request):
    return render(request,'solicitudes.html')