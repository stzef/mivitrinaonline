# -*- encoding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response 
from django.contrib.auth import login, logout, update_session_auth_hash, authenticate
from django.contrib.auth.models import User
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.template import RequestContext
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

import os
import json


from forms import *
from forms import loginForm,registroForm
from models import perfilUsuarioModel
from app.utilidades import get_or_none

def logoutView(request):
	logout(request)
	return redirect('/')

def profileView(request):
	profile = perfilUsuarioModel.objects.get(usuario_id = request.user.id)
	return render(request,'profile.html',{'profile': profile})

def loginEmail(request):
	form = emailLoginForm(request.POST or None)
	if form.is_valid():
		login(request,form.get_user())
	return render(request, 'loginEmail.html',{'form':form})

class registroView(FormView):
	form_class = registroForm
	template_name = 'signup.html'
	success_url = '/ingresar/'

	def form_valid(self,form):
		form.save()
		self.enviar_email_registro(form)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		return self.render_to_response(self.get_context_data(form=form))

	def enviar_email_registro(self, form):

		#obteniendo datos del formulario
		emailDeUsuario  = form.cleaned_data.get("email")
		nombreDeUsuario = form.cleaned_data.get("name")
		apellidoDeUsuario = form.cleaned_data.get("lastname")

		#datos para renderizar el template de email
		contextoDeTemplateParaEmail = {
			'usuario' : nombreDeUsuario+' '+apellidoDeUsuario,
			'descripcion' : 'Te damos la bienvenida a oportunidapp, esperamos que puedas obtener gran provecho de esta herramienta',
		}

		#retorna el texto de el template renderizado
		template = render_to_string('registro_email_template.html',contextoDeTemplateParaEmail)

		#creando mensaje
		msg = EmailMessage(
			subject='Bienvenido',
			from_email='sistematizaref <sistematizaref@gmail.com>',
			to = [emailDeUsuario],
		)

		#template en mailchimp para el mensaje
		msg.template_name = 'Bienvenida'

		#contenido del template en mailchimp
		msg.template_content = {
			'std_content00' : template,
		}

		#enviando email
		msg.send()


# Vista generica para loggear a un usuario 
# Esta vista es por defecto el login principal de la aplicacion

class loginView(FormView):
	# parametros de clase 
	form_class = loginForm
	template_name = 'login.html'
	success_url = '/micuenta/'

	def form_valid(self, form):
		perfil = get_or_none(perfilUsuarioModel, usuario=form.user_cache)
		if perfil is not None:
			login(self.request, form.user_cache)
		else:
			form.add_error(None, 'Lo sentimos este usuario no esta registrado')
			return self.form_invalid(form)
		return super(loginView, self).form_valid(form)

	# Verifica si la url tiene un querystring con parametro next
	def get_success_url(self):
		if self.request.GET.get('next'):
			return self.request.GET.get('next')
		else:
			return super(loginView, self).get_success_url()

	def get_context_data(self, **kwargs):
		context = super(loginView, self).get_context_data(**kwargs)
		context['next'] = self.request.GET.get('next')
		return context


def EditProfile(request):
	pk = request.user.id
	queryset = perfilUsuarioModel.objects.get(usuario_id = pk)
	queryset2 = User.objects.get(id = pk)
	form = profileForm(instance = queryset)
	form_2 = userForm(instance = queryset2)
	return render_to_response('UpdateProfile.html', {'form':form, 'form_2':form_2}, context_instance=RequestContext(request))

def UpdateProfile(request):
	response = {}
	if request.POST:
		form = profileForm(request.POST)
		form_2 = userForm(request.POST)
		pk = request.user.id
		profile = perfilUsuarioModel.objects.get(usuario_id = pk)
		user = User.objects.get(id = pk)
		response['response'] = pk
		if form.is_valid() and form_2.is_valid():
			form = profileForm(request.POST, instance = profile)
			form_2 = userForm(request.POST, instance = user)
			form.save()
			form_2.save()
			response['response'] = "Exito al Actualizar tus Datos"
		else:
			response['response'] = form_2.errors
	else:
		response['response'] = 'Error al Actualizar'
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def EditPassword(request):
	form = passForm()
	return render(request, 'UpdatePass.html', {'form':form})

def UpdatePass(request):
	json_response = {}
	user =  User.objects.get(id = request.user.id)
	form = passForm(request.POST)
	if request.POST:
		if form.is_valid():
			user.set_password(request.POST['password_new'])
			user.save()
			json_response['message'] = 'Exito al Actualizar'
			json_response['type'] = 'success'
		else:
			json_response['message'] = 'Error al Actualizar'
			json_response['type'] = 'danger'
	else:
		json_response['message'] = 'Error al Actualizar'
		json_response['type'] = 'danger'
	return HttpResponse(json.dumps(json_response), content_type = 'application/json')

@csrf_exempt
@login_required
def cambiarFotoPerfil(request):
	user = perfilUsuarioModel.objects.get(usuario = request.POST['usuario_id'])
	photo = request.FILES['foto']

	if (user.usuario_id == request.user.id):
		if user.foto.name != 'usuarios/avatar/user.jpg':
			image_path = settings.MEDIA_ROOT +'/'+ user.foto.name
			os.remove(image_path)
		user.foto = photo
		user.save(update_fields=["foto"])

	response_data = {}
	response_data['message'] = 'OK !!!!'
	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)


# Responde si la solicitud es ajax: '1' si usuario esta loggeado '0' si no
def is_auth_ajax(request):

	if request.is_ajax():
		# verificar si usuario esta autenticado
		if request.user.is_authenticated():
			auth = 1
		else:
			auth = 0
		# retorna json
		return JsonResponse({'auth':auth},safe=False)


# Loggea al usuario a traves de una solicitud ajax
def login_ajax(request):

	if request.is_ajax():
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(
			username = username,
			password = password,
		)
		if user is not None:
			if user.is_active:
				login(request, user)
			else:
				return JsonResponse(
					{'estado': 0, 'msg':'Este usuario no esta activo'}, 
					safe=False,
				)
			return JsonResponse(
						{'estado': 2, 'msg':''}, 
						safe=False,
					)
		else:
			return JsonResponse(
						{
							'estado': 1, 
							'msg': u'Por favor, introduce un nombre de usuario y clave correctos. Observa que ambos campos pueden ser sensibles a mayúsculas'
						}, 
						safe=False,
					)