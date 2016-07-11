from habilidades.views import habilidadesListView
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

	#url(r'^habilidades/$','habilidades.views.habilidadesViewTemplate',name='habilidades'),
	url(r'^habilidades/$',habilidadesListView.as_view(),name='habilidades'),
	url(r'^habilidades/(?P<slug>[\w\-]+)/(?P<pk>[\w]+)/$','habilidades.views.detalle',name='detalle'),
	url(r'^nuevahabilidad/$','habilidades.views.crearNuevaHabilidad',name='nuevaHabilidad'),

	url(r'^fotohabilidad/$','habilidades.views.cambiarFotoHabilidad',name='fotoHabilidad'),
	url(r'^desactivarhabilidad/$','habilidades.views.desactivarHabilidad',name='desactivarHabilidad'),
	url(r'^activarhabilidad/$','habilidades.views.activarHabilidad',name='activarHabilidad'),
	url(r'^editarhabilidad/$','habilidades.views.editarHabilidad',name='editarHabilidad'),

	url(r'^datosdecontacto/$','habilidades.views.obtener_datos_de_contacto',name='datosdecontacto'),
)
