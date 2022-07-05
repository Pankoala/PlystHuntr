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
   playlists = Playlist.objects.all()

   context = {
      "playlists": playlists,
   }

   return render(request, "ph_app/index.html", context)


def catalogo(request):
   """ Vista para atender la petición de la url /catálogo/ """
   return render(request, "ph_app/catalogo.html")


def playlist(request):
   """ Vista o función que atiende la url GET /playlist/"""
   playlists = Playlist.objects.all()
   playlister = Playlister.objects.all()
      
   context = {
      "playlists": playlists,
      "playlister" : playlister,
   }
   return render(request, "ph_app/playlist.html", context)


def playlist_add(request):
   """ Vista para atender la petición GET, POST de la url /playlist/add/ """
   if request.method == "POST":
      nombre = request.POST["nombre"]
      plataforma = request.POST["plataforma"]
      link = request.POST["link"]
      mood = request.POST["mood"]
      tag1 = request.POST["tag1"]
      tag2 = request.POST["tag2"]
      descripcion = request.POST["descripcion"]   

      nueva_playlist = Playlist(
         nombre=nombre,
         plataforma=plataforma,
         link=link,
         mood=mood,
         tag1=tag1,
         tag2=tag2,
         descripcion=descripcion,
      )
      nueva_playlist.save()
      return redirect("/")

   else:
       return render(request, "ph_app/playlist_add.html")


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

# def logout_usuario(request):
#     """Vista o función que atiende la url GET /logout"""
#     logout(request)

#     return redirect("/")

def register_usuario(request):
   """ Vista para atender la petición de la url /register/ """
   return render(request, "ph_app/register.html")


   #  """Vista o función que atiende la url GET /login/"""
   #  if request.method == 'POST':
   #      user = request.POST["user"]
   #      password = request.POST["password"]
   #      next = request.GET.get("next", "/")
   #      acceso = authenticate(username=user, password=password)
   #      print("user", user)
   #      print("password", password)
   #      print("next", next)
   #      print("acceso", acceso)
   #      if acceso != None:
   #          login(request,acceso)
   #          return redirect (next)
   #      else:
   #          msg = "Datos incorrectos, intente de nuevo"
   #  else:
   #      msg = ""

   #  return render(request, 'ph_app/login.html', {"msg": msg})