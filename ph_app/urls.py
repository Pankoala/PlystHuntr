from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path("login/", views.login_usuario, name="login"),
    path("playlist/", views.playlist, name="playlist"),
    path("subirpl/", views.playlist, name="subirpl"),
]