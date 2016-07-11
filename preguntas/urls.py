from django.conf.urls import patterns, include, url
from preguntas.views import listarPreguntasHechasPorUsuario,listarPreguntasRecibidasPorUsuario


urlpatterns = patterns('',
	url(r'^preguntanueva/$','preguntas.views.preguntanueva',name='preguntanueva'),
	url(r'^preguntas-hechas/$',listarPreguntasHechasPorUsuario.as_view(),name='preguntasHechas'),
	url(r'^preguntas-recibidas/$',listarPreguntasRecibidasPorUsuario.as_view(),name='preguntasRecibidas'),

	)
