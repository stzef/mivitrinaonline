from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from views import *
from usuarios import views
from usuarios.forms import SetPasswordForm


urlpatterns = patterns('',
	url(r'^perfil/$','usuarios.views.profileView',name='profile'),
	url(r'^perfil/edit/$','usuarios.views.EditProfile',name='edit-profile'),
	url(r'^perfil/edit-password/$','usuarios.views.EditPassword', name='edit-password'),
	url(r'^perfil/profile-update/$','usuarios.views.UpdateProfile',name='update-profile'),
	url(r'^perfil/password-update/$','usuarios.views.UpdatePass',name='update-password'),
	url(r'^perfil/foto-usuario/$','usuarios.views.cambiarFotoPerfil',name='fotoPerfil'),


	url(r'^isauthajax/$','usuarios.views.is_auth_ajax',name='is_auth_ajax'),
	url(r'^ingresarajax/$','usuarios.views.login_ajax',name='login_ajax'),

	url(r'^registro/$',registroView.as_view(),name='registro'),
	url(r'^ingresar/$',loginView.as_view(),name='ingresar'),
	url(r'^salir/$','usuarios.views.logoutView',name='salir'),


	url(
			r'^recuperar-cuenta/$',
			'django.contrib.auth.views.password_reset',
			{
				'template_name': 'solicitud_cambio_password_email.html',
			},
			name='recuperar-cuenta'
		),


	url(
			r'^recuperar-cuenta/verificado/$',
			'django.contrib.auth.views.password_reset_done',
			{
				'template_name' : 'solicitud_cambio_password_hecho.html',
			},
			name='password_reset_done'
		),

	url(
			r'^recuperar-cuenta/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
			'django.contrib.auth.views.password_reset_confirm',
			{
				'template_name' : 'cambio_password_confirmacion.html',
				'set_password_form' : SetPasswordForm,
			},
			name='password_reset_confirm'
		),


	url(
			r'^recuperar-cuenta/hecho/$',
			'django.contrib.auth.views.password_reset_complete',
			{
				'template_name' : 'cambio_password_hecho.html'
			},
			name='password_reset_complete'
		),

)