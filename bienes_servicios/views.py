# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import get_object_or_404
from django.template import defaultfilters
from django.utils import timezone
from django.core.urlresolvers import reverse

#Importaciones desde Aplicacion
from models import bienesServiciosModel, categoriasModel
from forms import *
from usuarios.models import perfilUsuarioModel
from app.utilidades import cleanJsonModel
from mivitrinaonline.settings import BASE_DIR
from app.utilidades import get_or_none
from estadisticas.models import bienesServiciosSolicitadosModel

#Importaciones desde Python
import json
import os

#Importaciones de otras librerias
from braces.views import LoginRequiredMixin

class bienesServiciosListView(LoginRequiredMixin, ListView):
	login_required = True
	model = bienesServiciosModel
	template_name = 'bienes_servicios.html'
	context_object_name = 'bienes_servicios'
	form = nuevoBienServicioForm

	def getCantidadActivas(self):
		cantidadActivas = bienesServiciosModel.objects.filter(usuario__usuario__username=self.request.user.username, estado=True).count()
		return cantidadActivas

	def getInactivos(self):
		inactivas = bienesServiciosModel.objects.filter(usuario__usuario__username=self.request.user.username,estado=False).order_by('-fecha_creacion')
		return inactivas

	def get_queryset(self):
		queryset = bienesServiciosModel.objects.filter(usuario__usuario__username=self.request.user.username, estado=True).order_by('-fecha_creacion')
		return queryset

	def get(self, request, *args, **kwargs):
		return super(bienesServiciosListView, self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(bienesServiciosListView, self).get_context_data(**kwargs)
		context['form'] = self.form
		context['inactivas'] = self.getInactivos()
		context['cantidadInactivas'] = context['inactivas'].count()
		context['cantidadActivas'] = self.getCantidadActivas()
		return context

@login_required()
def crearNuevoBienServicio(request):
	if request.is_ajax():
		form = nuevoBienServicioForm(request.POST)
		response_data = {}
		if form.is_valid():
			bienServicioNuevo = form.save(commit=False)
			usuario = perfilUsuarioModel.objects.get(pk=request.user.id)
			bienServicioNuevo.usuario = usuario

			slugFind = bienesServiciosModel.objects.filter(slug=defaultfilters.slugify(bienServicioNuevo.slug))

			print(slugFind)

			try:
				bienServicioNuevo.save()
				response_data['id'] = bienServicioNuevo.pk
				response_data['nBienServicio'] = bienServicioNuevo.nBienServicio
				response_data['slug'] = bienServicioNuevo.slug
				response_data['descripcion'] = bienServicioNuevo.descripcion
				response_data['categoria'] = bienServicioNuevo.categoria.categoria
				response_data['val_promedio'] = bienServicioNuevo.val_promedio
				response_data['num_solicitudes'] = bienServicioNuevo.num_solicitudes
				response_data['precio'] = bienServicioNuevo.precio
				response_data['foto'] = bienServicioNuevo.foto.url
				return JsonResponse(response_data, safe=False)
			except Exception, e:
				#print(type(e))
				response_data['error'] = e.message
				return JsonResponse(response_data, safe=False)


		else:
			return JsonResponse(form.errors.as_json(), safe=False)

#V iew encargada de retornar template del detalle de un Bien/Servicio
@login_required()
def detalle(request, slug, pk):

	try:
		bienServicioBuscado = bienesServiciosModel.objects.get(slug=slug, pk=pk)
	except ObjectDoesNotExist:
		bienServicioBuscado = get_object_or_404(bienesServiciosModel,pk=pk)

	templateRespuesta = 'no_permitido.html'
	form = nuevoBienServicioForm(instance=bienServicioBuscado)

	if bienServicioBuscado.usuario_id == request.user.id:
		templateRespuesta = 'detalle.html'
		contexto = {
			'bienServicio': bienServicioBuscado,
			'form' : form,
		}
		return render(request,templateRespuesta, contexto)
	return render(request,templateRespuesta)

# View encargada editar una Bien/Servicio
@login_required()
def editarBienServicio(request):
	if request.method == "POST":
		form = nuevoBienServicioForm(request.POST)
		response_data = {}
		if form.is_valid():
			bienServicioEditar = bienesServiciosModel.objects.get(id=request.POST['id'])
			if bienServicioEditar.usuario_id == request.user.id:
				bienServicioEditar.nBienServicio = request.POST['nBienServicio']
				bienServicioEditar.descripcion = request.POST['descripcion']
				bienServicioEditar.precio = request.POST['precio']
				print timezone.now()
				bienServicioEditar.fecha_actualizacion = timezone.now()
				bienServicioEditar.save(update_fields=['nBienServicio','descripcion','precio','fecha_actualizacion'])

				response_data['message'] = 'Edición exitosa'
				return HttpResponse(
					json.dumps(response_data),
					content_type="application/json"
				)
			else:
				return render(request,'no_permitido.html')
		else:
			print form.is_valid()
			response_data['message'] = 'error formulario'
			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)

# View encargada desactivar un Bien/Servicio
@login_required()
def desactivarBienServicio(request):
	if request.is_ajax() and request.method == "POST":
		bienServicio_id = request.POST['id']
		bienServicioDesactivar = get_object_or_404 (bienesServiciosModel,id = bienServicio_id)
		response_data = {}

		if bienServicioDesactivar.usuario_id == request.user.id:
			bienServicioDesactivar.estado = False
			bienServicioDesactivar.save(update_fields=["estado"])

			response_data['message'] = 'Bien/Servicio activada'

			return HttpResponse(
				json.dumps(response_data),
				content_type="application/json"
			)
		else:
			return render(request,'no_permitido.html')
	else:
		return render(request,'no_permitido.html')

@login_required()
def activarBienServicio(request):
	if request.is_ajax() and request.method == "POST":
		bienServicio_id = request.POST['id']
		bienServicioActivar = get_object_or_404 (bienesServiciosModel,id = bienServicio_id)
		if bienServicioActivar.usuario_id == request.user.id:
			response_data = {}
			bienServicioActivar.estado = True
			bienServicioActivar.save(update_fields=["estado"])

			response_data['message'] = 'Bien/Servicio activada'
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
def cambiarFotoBienServicio(request):

	#Obtener Parametros
	bienServicioCambiarFoto = bienesServiciosModel.objects.get(id=request.POST['id'])
	imagenRecibida = request.FILES['foto']
	imagenRecibida.name = bienServicioCambiarFoto.nBienServicio.replace(' ','_')+str(bienServicioCambiarFoto.id)
	response_data = {}
	if bienServicioCambiarFoto.usuario_id == request.user.id:
		borrarFotoActual(bienServicioCambiarFoto)
		bienServicioCambiarFoto.foto = imagenRecibida
		bienServicioCambiarFoto.fecha_actualizacion = timezone.now()
		bienServicioCambiarFoto.save(update_fields=["foto","fecha_actualizacion"])
	else:
		response_data['error'] = "No tiene permitido cambiar imagen de otros."

	return HttpResponse(
		json.dumps(response_data),
		content_type="application/json"
	)

# Borra la foto actual en Disco
def borrarFotoActual(bienServicio):
	archivoPath = BASE_DIR+bienServicio.foto.url
	imgPorDefecto = '/media/bienes_servicios/img/no_image.png'
	if bienServicio.foto.url != imgPorDefecto and os.path.isfile(archivoPath):
		os.remove(archivoPath)

# Responde en json los datos de contacto de la persona para un Bien/Servicio especifica
def obtener_datos_de_contacto(request):
	if request.is_ajax():
		bienServicio_id = request.GET.get('id',None)
		bienServicio = get_or_none(bienesServiciosModel,id=bienServicio_id)
		if bienServicio is not None:
			response_data = {}
			response_data['celular1'] = bienServicio.usuario.celular1
			response_data['celular2'] = bienServicio.usuario.celular2
			response_data['celular3'] = bienServicio.usuario.celular3
			response_data['coordenadas'] = { 'lat': float(bienServicio.usuario.coordenadas.split(",")[0]) ,'lng': float(bienServicio.usuario.coordenadas.split(",")[1]) }
			response_data['email'] = bienServicio.usuario.usuario.email

			hs = bienesServiciosSolicitadosModel()
			hs.bien_servicio = bienServicio
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

class bienServicioComentarioView(CreateView):
	template_name = 'form_general.html'
	success_message = 'Comentario agregado correctamente'
	form_class = ComentarioForm

	def get_context_data(self, **kwargs):
		context = super(bienServicioComentarioView, self).get_context_data(**kwargs)
		context['title'] = 'Agregar comentario'
		context['url'] = reverse('comentario', kwargs = {'slug': self.kwargs['slug']})
		return context

	def form_valid(self, form):
		form.instance.usuario = self.request.user
		form.instance.bienServicio = bienesServiciosModel.objects.get(slug =  self.kwargs['slug'])
		form.save()
		return super(bienServicioComentarioView, self).form_valid(form)

	def get_success_url(self):
		return reverse('detallebusqueda', kwargs = {'slug': self.kwargs['slug']})

def comentario_eliminar(request, pk):
	response = {}
	comentario = comentariosBienesServiciosModel.objects.get(pk = pk).delete()
	response['type'] = 'success'
	response['msg'] = 'Exito al eliminar el comentario'
	return HttpResponse(json.dumps(response), "application/json")