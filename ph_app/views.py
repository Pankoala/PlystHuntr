from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests

from .models import Playlister, Playlist

# Create your views here.
def index(request):
   """ Vista para atender la petición de la url / """
   return render(request, "ph_app/index.html")


def catalogo(request):
   """ Vista o función que atiende la url GET /catalogo/ """
   playlist = Playlist.objects.get(nombre = "Random")
   url_image = ""
   if playlist.plataforma == "SP":
      html = requests.get(playlist.link).text
      soup = BeautifulSoup(html, 'html.parser')
      meta = soup.find(property = "og:image")
      url_image = meta.attrs["content"]
      id_spotify = playlist.link.split("?")[0].split("/")[-1]
      url_playlist = f"https://open.spotify.com/embed/playlist/{id_spotify}"
   elif playlist.plataforma == "DZ":
      url_playlist = ""
   elif playlist.plataforma == "TD":
      url_playlist = ""
   return render(request, "ph_app/catalogo.html", {"url_playlist": url_playlist, "playlist": playlist, "url_image" : url_image})



# def login(request):
#     """ Vista o función que atiende la url GET /login/ """
#     return render(request, "ph_app/login.html")

def login_usuario(request):
    """Vista o función que atiende la url GET /login/"""
    if request.method == 'POST':
        user = request.POST["user"]
        password = request.POST["password"]
        next = request.GET.get("next", "/")
        acceso = authenticate(username=user, password=password)
        print("user", user)
        print("password", password)
        print("next", next)
        print("acceso", acceso)
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