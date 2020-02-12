from django.contrib import admin
from .models import *

class TableroAdmin(admin.ModelAdmin):
    list_display=('nombreTab',)

class ListaAdmin(admin.ModelAdmin):
    list_display=('nombreList','fkTablero')

class TarjetaAdmin(admin.ModelAdmin):
    list_display=('nombreTarj','descripcion','fkLista')

admin.site.register(Tablero,TableroAdmin)
admin.site.register(Lista,ListaAdmin)
admin.site.register(Tarjeta,TarjetaAdmin)