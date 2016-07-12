from django.conf.urls import patterns, include, url

from app.views import miCuentaView

urlpatterns = patterns('',
	url(r'^$', 'app.views.inicio',name='inicio'),
	url(r'^404/$', 'app.views.view_404',name='404'),
	url(r'^500/$', 'app.views.view_500',name='500'),
	url(r'^micuenta/$',miCuentaView.as_view() , name='miCuenta'),
)
