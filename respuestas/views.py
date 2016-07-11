# -*- encoding: utf-8 -*-
from django.shortcuts import render 
from django.http import JsonResponse


from respuestas.models import respuestasModel
from preguntas.models import preguntasModel
from app.utilidades import get_or_none


def crearRespuesta(request):
	if request.is_ajax():
		pregunta_id = request.POST['pregunta']
		respuesta   = request.POST['respuesta']
		pregunta = get_or_none(preguntasModel, id=pregunta_id)

		if pregunta is not None:
			nuevaRespuesta = respuestasModel(pregunta=pregunta,respuesta=respuesta)
			nuevaRespuesta.save()

			pregunta.respuesta = nuevaRespuesta
			pregunta.save(update_fields=['respuesta'])

			nuevaRespuesta.enviar_respuesta_email()

			mensaje = 'Listo su mensaje a sido enviado.'

		else:

			mensaje = 'Lo sentimos no puede responder por el momento, inténtelo mas tarde.'

		return JsonResponse(
			{
				'mensaje': mensaje,
			},
			safe = False,

		)
