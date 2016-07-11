from django.conf.urls import patterns, include, url
from busquedas.views import *

urlpatterns = patterns('',

	url(r'^buscar/$', 'busquedas.views.buscarView', name='buscar'),
	url(r'^buscar/(?P<slug>[\w\-]+)/$', busquedasCategoriaLista.as_view(), name='busqueda'),
	url(r'^b/dt/(?P<slug>[\w\-]+)/$',detalleHabilidadBuscada.as_view(), name='detallebusqueda'),
	url(r'^b/pl/(?P<busqueda>[\w\ ]+)/$',busquedasPorPalabraLista.as_view(), name='busquedaPalabra')
	)
