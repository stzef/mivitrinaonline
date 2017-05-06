from django.conf.urls import patterns, include, url
from busquedas import views

urlpatterns = patterns('',
	url(r'^buscar/$', views.buscarView, name='buscar'),
	url(r'^buscar/(?P<slug>[\w\-]+)/$', views.busquedasCategoriaLista.as_view(), name='busqueda'),
	url(r'^b/dt/(?P<slug>[\w\-]+)/$',views.detalleBienServicioBuscada.as_view(), name='detallebusqueda'),
	url(r'^b/pl/(?P<busqueda>[\w\ ]+)/$',views.busquedasPorPalabraLista.as_view(), name='busquedaPalabra')
)
