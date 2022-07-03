from bs4 import BeautifulSoup
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from requests_html import HTMLSession
import requests

from .models import Playlister, Playlist

# Create your views here.
def index(request):
   """ Vista o función que atiende la url GET /playlist/"""
   playlist = Playlist.objects.get(nombre = "Saturn Waves")
   url_image = ""
   if playlist.plataforma == "SP":
      html = requests.get(playlist.link).text
      soup = BeautifulSoup(html, 'html.parser')
      meta = soup.find(property = "og:image")
      url_image = meta.attrs["content"]
      id_spotify = playlist.link.split("?")[0].split("/")[-1]
      url_playlist = f"https://open.spotify.com/embed/playlist/{id_spotify}"

   elif playlist.plataforma == "DZ":
      html = requests.get(playlist.link).text
      soup = BeautifulSoup(html, 'html.parser')
      meta = soup.find(property = "og:image")
      url_image = meta.attrs["content"]
      og_deezer = soup.find(property = "og:url")
      url_deezer = og_deezer.attrs["content"]
      id_deezer = url_deezer.split("/")[-1]
      url_playlist = f"https://widget.deezer.com/widget/dark/playlist/{id_deezer}"

   elif playlist.plataforma == "TD":
      # session = HTMLSession()
      # html = session.get(playlist.link).text
      # soup = BeautifulSoup(html, 'html.parser')
      # meta = soup.find(property == "og:image")
      # url_image = meta.attrs["content"]
      id_tidal = playlist.link.split("/")[-1]
      url_playlist = f"https://embed.tidal.com/playlists/{id_tidal}?layout=gridify"

   playlists_all = Playlist.objects.all()
      
   return render(request, "ph_app/index.html", {"url_playlist": url_playlist, "playlist": playlist, "url_image" : url_image, "playlists": playlists_all,})


def catalogo(request):
   """ Vista para atender la petición de la url /catálogo/ """
   return render(request, "ph_app/catalogo.html")


def subirpl(request):
   """ Vista para atender la petición de la url /subirpl/ """
   return render(request, "ph_app/subirpl.html")


def playlist(request):
   """ Vista o función que atiende la url GET /playlist/"""
   playlist = Playlist.objects.get(nombre = "Tik Toks Latinos")
   url_image = ""
   if playlist.plataforma == "SP":
      html = requests.get(playlist.link).text
      soup = BeautifulSoup(html, 'html.parser')
      meta = soup.find(property = "og:image")
      url_image = meta.attrs["content"]
      id_spotify = playlist.link.split("?")[0].split("/")[-1]
      url_playlist = f"https://open.spotify.com/embed/playlist/{id_spotify}"

   elif playlist.plataforma == "DZ":
      html = requests.get(playlist.link).text
      soup = BeautifulSoup(html, 'html.parser')
      meta = soup.find(property = "og:image")
      url_image = meta.attrs["content"]
      og_deezer = soup.find(property = "og:url")
      url_deezer = og_deezer.attrs["content"]
      id_deezer = url_deezer.split("/")[-1]
      url_playlist = f"https://widget.deezer.com/widget/dark/playlist/{id_deezer}"

   elif playlist.plataforma == "TD":
      # session = HTMLSession()
      # html = session.get(playlist.link).text
      # soup = BeautifulSoup(html, 'html.parser')
      # meta = soup.find(property == "og:image")
      # url_image = meta.attrs["content"]
      id_spotify = playlist.link.split("/")[-1]
      url_playlist = f"https://embed.tidal.com/playlists/{id_spotify}?layout=gridify"

   playlists_all = Playlist.objects.all()
   playlister = Playlister.objects.all()
      
   return render(request, "ph_app/playlist.html", {"url_playlist": url_playlist, "playlist": playlist, "url_image" : url_image, "playlists": playlists_all, "playlister" : playlister})

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