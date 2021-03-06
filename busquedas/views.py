# -*- encoding: utf-8 -*-
# Importaciones desde Django
from django.shortcuts import render
from django.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView
from django.db.models import Q

#Importaciones desde Aplicacion [Oportunidad]
from bienes_servicios.models import bienesServiciosModel, categoriasModel
from usuarios.models import perfilUsuarioModel

#Importaciones desde Python
import json

class detalleBienServicioBuscada(DetailView):
	model = bienesServiciosModel
	context_object_name = 'bienServicio'
	template_name = 'busqueda_detalle.html'

	#retorna elementos recomendados del modelo 'bienesServiciosModel'
	def getRecomendados(self, BienServicio):
		recomendados = bienesServiciosModel.objects.filter(categoria=BienServicio.categoria,estado=True).exclude(id=BienServicio.id).order_by('-val_promedio')[:3]
		return recomendados

	#retorna elementos los otros bienes y servicios del mismo usuario
	def getBienesServiciosUsuario(self, BienServicio):
		#bienesServicioUsuario = bienesServiciosModel.objects.filter(usuario=BienServicio.usuario.usuario,estado=True).exclude(id=BienServicio.id)[:3]
		bienesServicioUsuario = bienesServiciosModel.objects.filter(usuario=BienServicio.usuario.usuario.pk).exclude(id=BienServicio.id)[:3]
		print bienesServicioUsuario
		return bienesServicioUsuario

	#incluye elementos dentro del contexto y los retorna
	def get_context_data(self, **kwargs):
		context = super(detalleBienServicioBuscada, self).get_context_data(**kwargs)
		context['object'].numero_visita = (context['object'].numero_visita + 1)
		context['object'].save()
		recomendados = self.getRecomendados(context['object'])
		bienesServicioUsuario = self.getBienesServiciosUsuario(context['object'])
		context['recomendados'] = recomendados
		context['bienesServicioUsuario'] = bienesServicioUsuario
		return context

class busquedasCategoriaLista(ListView):

	#atributos de la clase
	model = bienesServiciosModel
	paginate_by = 10
	template_name = 'busqueda.html'
	context_object_name = 'bienes_servicios'
	ordering = '-val_promedio'

	#lista guarda los tipos de ordenamiento que se implementan para las busquedas
	ordenList = [
		('','-val_promedio','Mas valoradas'),
		('PRECIO_DESC','-precio','Mayor precio'),
		('PRECIO','precio','Menor precio'),
	]


	#recibe un indice y lo compara con el primer elemento de los elementos de ordenList
	#si exite retorna el elemento
	def get_elemento_busqueda(self, indice):
		i = 0
		for a,b,c in self.ordenList:
			if a == indice:
				return self.ordenList[i]
			i += 1

	#configura el orden para aplicarlo a los elementos del listView
	#varifica si recibe el parametro 'orden' en la url y retorna el nombre del campo
	#a ordenar si no retorna el atributo 'ordering' de la clase
	def get_ordering(self):
		orden = self.request.GET.get('orden')
		if orden is not None:
			item = self.get_elemento_busqueda(orden)
			return item [1]
		else:
			return self.ordering


	#retorna el orden actual de los elementos del listView
	def get_orden_actual(self):
		orden = self.request.GET.get('orden')
		if orden is not None:
			item = self.get_elemento_busqueda(orden)
			return item
		else:
			return self.ordenList[0]

	#recibe un queryset y una frase
	#filtra los elementos del queryset segun las palabras de la frase
	def query_por_palabra(self, queryset, busqueda):

		dicbusqueda = busqueda.split()

		for palabra in dicbusqueda:
			if queryset.filter(Q(nBienServicio__icontains=palabra) | Q(descripcion__icontains=palabra)).exists():
				queryset = queryset.filter(Q(nBienServicio__icontains=palabra) | Q(descripcion__icontains=palabra))
			else:
				pass
				#queryset = categoriasModel.objects.none()
		return queryset

	#retorna los elementos  del modelo 'bienesServiciosModel' segun la consulta
	def get_queryset(self):
		categoria = categoriasModel.objects.get(slug=self.kwargs['slug'])
		queryset = self.model.objects.filter(estado=True,categoria=categoria)

		busqueda = self.request.GET.get('q')
		if busqueda is not None:
			queryset = self.query_por_palabra(queryset, busqueda)

		ordering = self.get_ordering()

		if ordering:
			queryset = queryset.order_by(ordering)

		return queryset


	#incluye elementos dentro del contexto y lo retorna
	def get_context_data(self, **kwargs):

		context = super(busquedasCategoriaLista, self).get_context_data(**kwargs)
		categoria = categoriasModel.objects.get(slug=self.kwargs['slug'])
		ordenItem = self.get_orden_actual()
		busqueda = self.request.GET.get('q')
		todasCategorias = categoriasModel.objects.all().order_by('categoria')

		if busqueda is not None:
			busqueda = busqueda.replace(' ','+')

		context['todasCategorias']	 = todasCategorias
		context['categoria']		 = categoria
		context['ordenList']		 = self.ordenList
		context['ordenActual']		 = ordenItem[2]
		context['orden']			 = ordenItem[0]
		context['busqueda']			 = busqueda
		context['page']				 = self.request.GET.get('page')

		return context

class busquedasPorPalabraLista(ListView):
	model = bienesServiciosModel
	paginate_by = 10
	context_object_name = 'bienes_servicios'
	template_name = 'busqueda_palabras.html'
	ordering = '-val_promedio'

	ordenList = [
		('','-val_promedio','Mas valoradas'),
		('PRECIO_DESC','-precio','Mayor precio'),
		('PRECIO','precio','Menor precio'),
	]


	def get_elemento_busqueda(self, indice):
		i = 0
		for a,b,c in self.ordenList:
			if a == indice:
				return self.ordenList[i]
			i += 1


	def get_ordering(self):
			orden = self.request.GET.get('orden')
			if orden is not None:
				item = self.get_elemento_busqueda(orden)
				return item [1]
			else:
				return self.ordering


	def get_orden_actual(self):
			orden = self.request.GET.get('orden')
			if orden is not None:
				item = self.get_elemento_busqueda(orden)
				return item
			else:
				return self.ordenList[0]


	def get_queryset(self):
		busqueda = self.kwargs['busqueda']
		if busqueda is not None:
			queryset = bienesServiciosModel.objects.filter(estado=True)
			queryset = self.query_por_palabra(queryset, busqueda)

			ordering = self.get_ordering()
			if ordering:
				queryset = queryset.order_by(ordering)

			return queryset


	def query_por_palabra(self, queryset, busqueda):

		dicbusqueda = busqueda.split()

		for palabra in dicbusqueda:
			if queryset.filter(Q(nBienServicio__icontains=palabra) | Q(descripcion__icontains=palabra)).exists():
				queryset = queryset.filter(Q(nBienServicio__icontains=palabra) | Q(descripcion__icontains=palabra))
			else:
				pass
				#queryset = categoriasModel.objects.none()
		return queryset


	def get_context_data(self, **kwargs):
		context = super(busquedasPorPalabraLista, self).get_context_data(**kwargs)
		ordenItem = self.get_orden_actual()
		todasCategorias = categoriasModel.objects.all().order_by('categoria')

		context['todasCategorias']	 = todasCategorias
		context['busqueda']			 = self.kwargs['busqueda']
		context['algunasCategorias'] = self.get_algunas_categorias()
		context['ordenList'] 		 = self.ordenList
		context['ordenActual']  	 = ordenItem[2]
		context['orden'] 			 = ordenItem[0]
		context['page'] 			 = self.request.GET.get('page')

		return context


	def get_algunas_categorias(self):
		return categoriasModel.objects.all()[:10]

#[View]
#retorna el template
def buscarView(request):
	TodasLasCategorias = categoriasModel.objects.all().order_by('categoria')
	return render(request,'buscar.html',{'categorias':TodasLasCategorias})


