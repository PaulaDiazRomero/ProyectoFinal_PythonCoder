from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required 
from AppInicio.forms import *
from AppInicio.models import *

# Create your views here.
def inicio(request):
    return render(request, "AppInicio/inicio.html")


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            user = form.cleaned_data["Usuario"]
            contra = form.cleaned_data["Contraseña"]
            usuario = authenticate(username=user, password=contra)
            
            if usuario is not None:
                login(request, usuario)
                return render(request, "AppInicio/inicio.html")
            else:
                return render(request, "AppInicio/login.html", {"form": form})
        else:
            return render(request, "AppInicio/login.html", {"form": form})
    else:
        form = AuthenticationForm()
        return render(request, "AppInicio/login.html", {"form": form}) 


def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppInicio/inicio.html")
        else:
            return render(request, "AppInicio/registro.html", {"form": form})
    else:
        form = UserRegisterForm()
        return render(request, "AppInicio/registro.html", {"form": form})
