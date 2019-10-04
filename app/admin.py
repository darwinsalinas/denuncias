from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Distrito, EstadoDenuncia, TipoLugar, TipoDelito, Sexo, ColorPiel, Contextura, Municipio, Localidad, ObjetoUtilizado, ObjetoAfectado, PresuntoAutor, Victima, Testigo, Denuncia 

admin.site.unregister(Group)

admin.site.site_header = "SDPN"
admin.site.site_title = "SDPN"
admin.site.index_title = "Bienvenido a SDPN"


class PresuntoAutorInline(admin.TabularInline):
    model = PresuntoAutor
    extra = 1


class VictimaInline(admin.TabularInline):
    model = Victima
    extra = 1


class TestigoInline(admin.TabularInline):
    model = Testigo
    extra = 1


class ObjetoUtilizadoInline(admin.TabularInline):
    model = ObjetoUtilizado
    extra = 1


class ObjetoAfectadoInline(admin.TabularInline):
    model = ObjetoAfectado
    extra = 1




class DenunciaAdmin(admin.ModelAdmin):
    model = Denuncia
    inlines = [
        VictimaInline,
        PresuntoAutorInline,
        TestigoInline,
        ObjetoUtilizadoInline,
        ObjetoAfectadoInline,
    ]

    list_filter = ('fecha_hora', 'estado', 'localidad', 'tipo_delito', 'victima_set__sexo')


admin.site.register([
    Distrito, 
    EstadoDenuncia, 
    TipoLugar, 
    TipoDelito, 
    Sexo, 
    ColorPiel, 
    Contextura, 
    Municipio, 
    Localidad, 
    ObjetoUtilizado, 
    ObjetoAfectado, 
    PresuntoAutor, 
    Victima, 
    Testigo 
])

admin.site.register(Denuncia, DenunciaAdmin)
