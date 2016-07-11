# -*- encoding: utf-8 -*-
#importaciones dede Django
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView


#importaciones desde Aplicacion
from habilidades.models import habilidadesModel
from preguntas.models import preguntasModel
from usuarios.models import perfilUsuarioModel


#importaciones desde python


#Importaciones de otras librerias
from braces.views import LoginRequiredMixin


#View encargada de registrar una pregunta a un ofertante
#request en AJAX response en JSON
@csrf_exempt
def preguntanueva(request):
	if request.is_ajax():
		# recibe parametros
		habilidadPreguntada = habilidadesModel.objects.get(pk=request.POST['habilidad'])
		descripcionPregunta = request.POST['pregunta']
		solicitante = perfilUsuarioModel.objects.get(pk=request.user.id)

		# crear pregunta
		pregunta = preguntasModel(
			pregunta = descripcionPregunta,
			habilidad = habilidadPreguntada,
			ofertante = habilidadPreguntada.usuario,
			solicitante = solicitante,
		)

		# guardar pregunta
		pregunta.save()

		# enviar email de notificacion
		pregunta.enviar_pregunta_email()

		# respuesta
		return JsonResponse(
			{
				'estado': 1,
				'pregunta': pregunta.pregunta,
				'mensaje': 'Listo hemos enviado tu pregunta, te avisaremos con un email cuando respondan.',
			},
			safe= False,
		)


class listarPreguntasHechasPorUsuario(LoginRequiredMixin,ListView):
	model = preguntasModel
	template_name = 'lista_preguntas_hechas_por_usuario.html'
	context_object_name = 'preguntasRespondidas'
	#ordering = ''

	def get_queryset(self):

		perfil = perfilUsuarioModel.objects.get(usuario=self.request.user)
		queryset = self.model.objects.filter(solicitante=perfil).exclude(respuesta=None).order_by('-respuesta__fecha')

		return queryset

	def get_preguntas_no_respondidas(self):

		perfil = perfilUsuarioModel.objects.get(usuario=self.request.user)
		preguntasNoRespondidas = self.model.objects.filter(solicitante=perfil).exclude(respuesta__isnull=False).order_by('-fecha')

		return preguntasNoRespondidas

	def get_context_data(self, **kwargs):
		context = super(listarPreguntasHechasPorUsuario, self).get_context_data(**kwargs)
		context['preguntasNoRespondidas'] = self.get_preguntas_no_respondidas()

		return context



class listarPreguntasRecibidasPorUsuario(ListView):
	model = preguntasModel
	template_name = 'lista_preguntas_recibidas_por_usuario.html'
	context_object_name = 'preguntasRespondidas'


	def get_queryset(self):
		perfil = perfilUsuarioModel.objects.get(usuario=self.request.user)
		queryset = self.model.objects.filter(ofertante=perfil).exclude(respuesta=None).order_by('-respuesta__fecha')

		return queryset


	def get_preguntas_no_respondidas(self):

		perfil = perfilUsuarioModel.objects.get(usuario=self.request.user)
		preguntasNoRespondidas = self.model.objects.filter(ofertante=perfil).exclude(respuesta__isnull=False).order_by('-fecha')

		return preguntasNoRespondidas

	def get_context_data(self, **kwargs):
		context = super(listarPreguntasRecibidasPorUsuario, self).get_context_data(**kwargs)
		context['preguntasNoRespondidas'] = self.get_preguntas_no_respondidas()

		return context