from django.contrib import admin
from bienes_servicios.models import categoriasModel, bienesServiciosModel, comentariosBienesServiciosModel

admin.site.register(categoriasModel)
admin.site.register(bienesServiciosModel)
admin.site.register(comentariosBienesServiciosModel)