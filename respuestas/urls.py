from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
	url(r'^crear-respuesta/$','respuestas.views.crearRespuesta',name='crearRespuesta'),
)