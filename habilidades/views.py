# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404


#Importaciones desde Aplicacion [Oportunidad]
from models import habilidadesModel, habCategoriasModel
from forms import nuevaHabilidadForm
from usuarios.models import perfilUsuarioModel
from app.utilidades import cleanJsonModel
from mivitrinaonline.settings import BASE_DIR
from app.utilidades import get_or_none
from estadisticas.models import habilidadesSolicitadasModel

#Importaciones desde Python
import json
import os

#Importaciones de otras librerias
from braces.views import LoginRequiredMixin

class habilidadesListView(LoginRequiredMixin, ListView):
	login_required = True
	model = habilidadesModel
	template_name = 'habilidades.html'
	context_object_name = 'habilidades'
	form = nuevaHabilidadForm

	def getCantidadActivas(self):
		cantidadActivas = habilidadesModel.objects.filter(usuario=self.request.user, estado=True).count()
		return cantidadActivas

	def getHabilidadesInactivas(self):
		inactivas = habilidadesModel.objects.filter(usuario=self.request.user,estado=False).order_by('-fecha_creacion')
		return inactivas

	def get_queryset(self):
		queryset = habilidadesModel.objects.filter(usuario=self.request.user, estado=True).order_by('-fecha_creacion')
		return queryset

	def get(self, request, *args, **kwargs):
		return super(habilidadesListView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(habilidadesListView, self).get_context_data(**kwargs)
		context['form'] = self.form
		context['inactivas'] = self.getHabilidadesInactivas()
		context['cantidadInactivas'] = context['inactivas'].count()
		context['cantidadActivas'] = self.getCantidadActivas()
		return context

@login_required()
def crearNuevaHabilidad(request):	
	if request.is_ajax():
		form = nuevaHabilidadForm(request.POST)
		response_data = {}
		if form.is_valid():
			habilidadNueva = form.save(commit=False)
			usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
			habilidadNueva.usuario = usuario
			habilidadNueva.save()

			response_data['id'] = habilidadNueva.pk
			response_data['nhabilidad'] = habilidadNueva.nhabilidad
			response_data['slug'] = habilidadNueva.slug
			response_data['descripcion'] = habilidadNueva.descripcion
			response_data['categoria'] = habilidadNueva.categoria.categoria
			response_data['val_promedio'] = habilidadNueva.val_promedio
			response_data['num_solicitudes'] = habilidadNueva.num_solicitudes
			response_data['precio'] = habilidadNueva.precio
			response_data['foto'] = habilidadNueva.foto.url
			return JsonResponse(response_data, safe=False)

		else:
			return JsonResponse(form.errors.as_json(), safe=False)


#[detalleHabilidadView] View encargada de retornar template del detalle de una habilidad
@login_required()
def detalle(request, slug, pk):

	try:
		habilidadBuscada = habilidadesModel.objects.get(slug=slug, pk=pk)
	except ObjectDoesNotExist:
		habilidadBuscada = get_object_or_404(habilidadesModel,pk=pk)

	templateRespuesta = 'no_permitido.html'
	form = nuevaHabilidadForm(instance=habilidadBuscada)

	if habilidadBuscada.usuario_id == request.user.id:
		templateRespuesta = 'detalle.html'
		contexto = {
			'habilidad': habilidadBuscada,
			'form' : form,
		}
		return render(request,templateRespuesta, contexto)
	return render(request,templateRespuesta)


#[editarHabilidad] View encargada editar una habilidad
@login_required()
def editarHabilidad(request):
	if request.method == "POST":
		form = nuevaHabilidadForm(request.POST)
		if form.is_valid():
			habilidadParaEditar = habilidadesModel.objects.get(id=request.POST['id'])
			response_data = {}
			if habilidadParaEditar.usuario_id == request.user.id:
				habilidadParaEditar.nhabilidad = request.POST['nhabilidad']
				habilidadParaEditar.descripcion = request.POST['descripcion']
				habilidadParaEditar.precio = request.POST['precio']
				habilidadParaEditar.save(update_fields=['nhabilidad','descripcion','precio'])

				response_data['message'] = 'Edición exitosa'
				return HttpResponse(
					json.dumps(response_data),
					content_type="application/json"
				)
			else:
				return render(request,'no_permitido.html')
		else:
			response_data['message'] = 'error formulario'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)

#[desactivarHabilidad] View encargada desactivar una habilidad
@login_required()
def desactivarHabilidad(request):
	if request.is_ajax() and request.method == "POST":
		habilidad_id = request.POST['habilidad_id']
		habilidadPorDesactivar = get_object_or_404 (habilidadesModel,id = habilidad_id)
		response_data = {}

		if habilidadPorDesactivar.usuario_id == request.user.id:
			habilidadPorDesactivar.estado = False
			habilidadPorDesactivar.save(update_fields=["estado"])

			response_data['message'] = 'Habilidad activada'

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)
		else:
			return render(request,'no_permitido.html')
	else:
		return render(request,'no_permitido.html')

@login_required()
def activarHabilidad(request):
	if request.is_ajax() and request.method == "POST":
		habilidad_id = request.POST['habilidad_id']
		habilidadPorActivar = get_object_or_404 (habilidadesModel,id = habilidad_id)
		if habilidadPorActivar.usuario_id == request.user.id:
			response_data = {}
			habilidadPorActivar.estado = True
			habilidadPorActivar.save(update_fields=["estado"])

			response_data['message'] = 'Habilidad activada'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)

		else:
			return render(request,'no_permitido.html')
	else:
		return render(request,'no_permitido.html')


@csrf_exempt
@login_required
def cambiarFotoHabilidad(request):

	#Obtener Parametros
	habilidadCambioImagen = habilidadesModel.objects.get(id=request.POST['habilidad'])
	imagenRecibida = request.FILES['foto']
	imagenRecibida.name = habilidadCambioImagen.nhabilidad.replace(' ','_')+str(habilidadCambioImagen.id)
	response_data = {}
	if habilidadCambioImagen.usuario_id == request.user.id:
		borrarFotoActual(habilidadCambioImagen)
		habilidadCambioImagen.foto = imagenRecibida
		habilidadCambioImagen.save(update_fields=["foto"])
	else:
		response_data['error'] = "No tiene permitido cambiar imagen de otros."

	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)


#Borra la foto actual en Disco
def borrarFotoActual(habilidad):
	archivoPath = BASE_DIR+habilidad.foto.url
	imgPorDefecto = '/media/habilidades/img/no_image.png'
	if habilidad.foto.url != imgPorDefecto and os.path.isfile(archivoPath):
		os.remove(archivoPath)


#Responde en json los datos de contacto de la persona para una habilidad especifica
def obtener_datos_de_contacto(request):
	if request.is_ajax():
		habilidad_id = request.GET.get('habilidad',None)
		habilidad = get_or_none(habilidadesModel,id=habilidad_id)
		if habilidad is not None:
			response_data = {}
			response_data['celular1'] = habilidad.usuario.celular1
			response_data['celular2'] = habilidad.usuario.celular2
			response_data['celular3'] = habilidad.usuario.celular3
			response_data['email'] = habilidad.usuario.usuario.email

			hs = habilidadesSolicitadasModel(habilidad=habilidad)
			if request.user.is_authenticated():
				usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
				hs.usuario = usuario

			hs.save()

			return JsonResponse(
				response_data,
				safe=False,
			)

		else:
			response_data = {'msg':'Datos no encontrados'}
			return JsonResponse(
				response_data,
				safe=False,
			)
