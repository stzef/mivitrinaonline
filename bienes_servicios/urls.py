from bienes_servicios.views import bienesServiciosListView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#url(r'^habilidades/$','bienes_servicios.views.habilidadesViewTemplate',name='habilidades'),
	url(r'^habilidades/$',bienesServiciosListView.as_view(),name='habilidades'),
	url(r'^habilidades/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','bienes_servicios.views.detalle',name='detalle'),
	url(r'^nuevahabilidad/$','bienes_servicios.views.crearNuevoBienServicio',name='nuevaHabilidad'),

	url(r'^fotohabilidad/$','bienes_servicios.views.cambiarFotoBienServicio',name='fotoHabilidad'),
	url(r'^desactivarhabilidad/$','bienes_servicios.views.desactivarBienServicio',name='desactivarHabilidad'),
	url(r'^activarhabilidad/$','bienes_servicios.views.activarBienServicio',name='activarHabilidad'),
	url(r'^editarhabilidad/$','bienes_servicios.views.editarBienServicio',name='editarHabilidad'),

	url(r'^datosdecontacto/$','bienes_servicios.views.obtener_datos_de_contacto',name='datosdecontacto'),
)
