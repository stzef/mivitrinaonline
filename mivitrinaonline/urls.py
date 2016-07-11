from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', 'app.views.inicio',name='inicio'),
    url('', include('habilidades.urls')),
    url('', include('usuarios.urls')),
    url('', include('app.urls')),
    url('', include('preguntas.urls')),
    url('', include('respuestas.urls')),
    url('', include('busquedas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT,}
    ),
)
