from django.contrib import admin
from .models import Playlister, PlaylisterPlaylist


class PlaylisterAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "user", "fechaNacimiento", "genero")


class PlaylisterPlaylistAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("nombreplaylist", "mood", "canciones", "plataforma")

admin.site.register(Playlister, PlaylisterAdmin)
admin.site.register(PlaylisterPlaylist, PlaylisterPlaylistAdmin)
