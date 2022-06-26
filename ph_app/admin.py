from django.contrib import admin
from .models import Playlister, Playlist


class PlaylisterAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "user", "fechaNacimiento", "genero")


class PlaylistAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("nombre", "mood", "canciones", "plataforma")

admin.site.register(Playlister, PlaylisterAdmin)
admin.site.register(Playlist, PlaylistAdmin)
