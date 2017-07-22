from django.conf.urls import patterns, include, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from views import *
from django.contrib.auth import views as viewsauth
from usuarios import views
from usuarios.forms import SetPasswordForm


urlpatterns = patterns('',
	url(r'^perfil/$',views.profileView,name='profile'),
	url(r'^perfil/edit/$',views.EditProfile,name='edit-profile'),
	url(r'^perfil/edit-password/$',views.EditPassword, name='edit-password'),
	url(r'^perfil/profile-update/$',views.UpdateProfile,name='update-profile'),
	url(r'^perfil/password-update/$',views.UpdatePass,name='update-password'),
	url(r'^perfil/foto-usuario/$',views.cambiarFotoPerfil,name='fotoPerfil'),


	url(r'^isauthajax/$',views.is_auth_ajax,name='is_auth_ajax'),
	url(r'^ingresarajax/$',views.login_ajax,name='login_ajax'),

	url(r'^registro/$',registroView.as_view(),name='registro'),
	url(r'^ingresar/$',loginView.as_view(),name='ingresar'),
	url(r'^salir/$',views.logoutView,name='salir'),


	url(
			r'^recuperar-cuenta/$',
			viewsauth.password_reset,
			{
				'template_name': 'solicitud_cambio_password_email.html',
			},
			name='recuperar-cuenta'
		),


	url(
			r'^recuperar-cuenta/verificado/$',
			viewsauth.password_reset_done,
			{
				'template_name' : 'solicitud_cambio_password_hecho.html',
			},
			name='password_reset_done'
		),

	url(
			r'^recuperar-cuenta/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
			viewsauth.password_reset_confirm,
			{
				'template_name' : 'cambio_password_confirmacion.html',
				'set_password_form' : SetPasswordForm,
			},
			name='password_reset_confirm'
		),


	url(
			r'^recuperar-cuenta/hecho/$',
			viewsauth.password_reset_complete,
			{
				'template_name' : 'cambio_password_hecho.html'
			},
			name='password_reset_complete'
		),

)
