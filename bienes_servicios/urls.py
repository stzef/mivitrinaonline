#from bienes_servicios.views import bienesServiciosListView
from bienes_servicios.views import *
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	url(r'^bienes-servicios/$',bienesServiciosListView.as_view(),name='bienes-servicios'),
	url(r'^bienes-servicios/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$',detalle,name='detalle-bienes-servicios'),
	url(r'^nuevo-bien-servicio/$',crearNuevoBienServicio,name='nuevo-bien-servicio'),

	url(r'^foto-bien-servicio/$',cambiarFotoBienServicio,name='foto-bien-servicio'),
	url(r'^desactivar-bien-servicio/$',desactivarBienServicio,name='desactivar-bien-servicio'),
	url(r'^activar-bien-servicio/$',activarBienServicio,name='activar-bien-servicio'),
	url(r'^editar-bien-servicio/$',editarBienServicio,name='editar-bien-servicio'),
	url(r'^comentario/(?P<slug>[\w\-]+)/$',bienServicioComentarioView.as_view(),name='comentario'),
	url(r'^comentario-eliminar/(?P<pk>[\w]+)/$',comentario_eliminar,name='comentario_eliminar'),
	url(r'^datosdecontacto/$','bienes_servicios.views.obtener_datos_de_contacto',name='datosdecontacto'),
)
