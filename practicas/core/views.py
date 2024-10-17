from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth import authenticate

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

def salir(request):
    logout(request)
    return redirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Credenciales incorrectas.'})
    
    return render(request, 'login.html')