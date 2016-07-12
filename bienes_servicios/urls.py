from bienes_servicios.views import bienesServiciosListView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^bienes-servicios/$',bienesServiciosListView.as_view(),name='bienes-servicios'),
	url(r'^bienes-servicios/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','bienes_servicios.views.detalle',name='detalle-bienes-servicios'),
	url(r'^nuevo-bien-servicio/$','bienes_servicios.views.crearNuevoBienServicio',name='nuevo-bien-servicio'),

	url(r'^foto-bien-servicio/$','bienes_servicios.views.cambiarFotoBienServicio',name='foto-bien-servicio'),
	url(r'^desactivar-bien-servicio/$','bienes_servicios.views.desactivarBienServicio',name='desactivar-bien-servicio'),
	url(r'^activar-bien-servicio/$','bienes_servicios.views.activarBienServicio',name='activar-bien-servicio'),
	url(r'^editar-bien-servicio/$','bienes_servicios.views.editarBienServicio',name='editar-bien-servicio'),

	url(r'^datosdecontacto/$','bienes_servicios.views.obtener_datos_de_contacto',name='datosdecontacto'),
)
