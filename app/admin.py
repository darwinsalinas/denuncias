from django.contrib import admin
from django.contrib.auth.models import Group

from .models import ObjetoUtilizado

admin.site.unregister(Group)

admin.site.site_header = "SDPN"
admin.site.site_title = "SDPN"
admin.site.index_title = "Bienvenido a SDPN"


admin.site.register(ObjetoUtilizado)
