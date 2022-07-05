from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('login/', views.login_usuario, name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path('register/', views.register_usuario, name="register"),
    path('playlist/', views.playlist, name="playlist"),
    path('playlist/add/', views.playlist_add, name="playlist_add"),
]