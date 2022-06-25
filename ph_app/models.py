from django.db import models
from django.contrib.auth.models import User


# Django ya cuenta con una tabla de Usuario llamada User
# class User(models.Model):
#     username = models.CharField(max_length=80)
#     first_name = models.CharField(max_length=80)
#     last_name = models.CharField(max_length=80)
#     group = models.ForeignKey(Group)
#     email = models.EmailField()


# Create your models here.


class Playlister(models.Model):
    """ Define la tabla Playlister """
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        null=True, blank=True)
    fechaNacimiento = models.DateField(null=True, blank=True)
    GENERO = [
        ("H", "Hombre"),  # <- opcion
        ("M", "Mujer"),
        ("O", "Otro"),
    ]
    genero = models.CharField(max_length=1, choices=GENERO)  # VARCHAR(1)

    def __str__(self):
        return self.user.username


class PlaylisterPlaylist(models.Model):
    """ Define la tabla Playlister Playlist"""
    nombreplaylist = models.CharField(max_length=145)
    playlister = models.ForeignKey(Playlister, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=256)
    canciones = models.FloatField(default=0.0)
    MOOD = [
        ("Hap", "Happy"),
        ("Chi", "Chill"),
        ("Rom", "Romantic"),
        ("Blu", "Blue"),
    ]
    mood = models.CharField(max_length=3, choices=MOOD, null=True, blank=True)  # VARCHAR(2)
    PLATAFORMA = [
        ("DZ", "Deezer"),
        ("SP", "Spotify"),
        ("TD", "Tidal"),
        ("YT", "Youtube Music"),
    ]
    plataforma = models.CharField(max_length=2, choices=PLATAFORMA, null=True, blank=True)  # VARCHAR(2)
    link = models.CharField(max_length=100)


    def __str__(self):
        return str(self.nombreplaylist)

