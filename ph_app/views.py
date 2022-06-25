from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Playlister, PlaylisterPlaylist

# Create your views here.
def index(request):
   """ Vista para atender la petición de la url / """
   return render(request, "ph_app/index.html")


def catalogo(request):
    """ Vista o función que atiende la url GET /catalogo/ """
    return render(request, "ph_app/catalogo.html")



# def login(request):
#     """ Vista o función que atiende la url GET /catalogo/ """
#     return render(request, "ph_app/login.html")

def login_usuario(request):
    """Vista o función que atiende la url GET /login"""
    if request.method == 'POST':
        user = request.POST["user"]
        password = request.POST["password"]
        next = request.GET.get("next", "/")
        acceso = authenticate(user=user, password=password)
        if acceso != None:
            login(request,acceso)
            return redirect (next)
        else:
            msg = "Datos incorrectos, intente de nuevo"
    else:
        msg = ""

    return render(request, 'ph_app/login.html', {"msg": msg})

def logout_usuario(request):
    """Vista o función que atiende la url GET /logout"""
    logout(request)

    return redirect("/")