from bienes_servicios.views import habilidadesListView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#url(r'^habilidades/$','bienes_servicios.views.habilidadesViewTemplate',name='habilidades'),
	url(r'^habilidades/$',habilidadesListView.as_view(),name='habilidades'),
	url(r'^habilidades/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','bienes_servicios.views.detalle',name='detalle'),
	url(r'^nuevahabilidad/$','bienes_servicios.views.crearNuevaHabilidad',name='nuevaHabilidad'),

	url(r'^fotohabilidad/$','bienes_servicios.views.cambiarFotoHabilidad',name='fotoHabilidad'),
	url(r'^desactivarhabilidad/$','bienes_servicios.views.desactivarHabilidad',name='desactivarHabilidad'),
	url(r'^activarhabilidad/$','bienes_servicios.views.activarHabilidad',name='activarHabilidad'),
	url(r'^editarhabilidad/$','bienes_servicios.views.editarHabilidad',name='editarHabilidad'),

	url(r'^datosdecontacto/$','bienes_servicios.views.obtener_datos_de_contacto',name='datosdecontacto'),
)
