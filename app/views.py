from django.shortcuts import render
from django.views.generic import TemplateView

from usuarios.models import perfilUsuarioModel
from bienes_servicios.models import bienesServiciosModel

#Importaciones de otras librerias
from braces.views import LoginRequiredMixin

class miCuentaView(LoginRequiredMixin, TemplateView):
	template_name = 'mi_cuenta.html'
	login_required = True

	def get_context_data(self, **kwargs):

		perfil = perfilUsuarioModel.objects.get(usuario=self.request.user)

		context = super(miCuentaView, self).get_context_data(**kwargs)
		context['bienes_servicios_activos'] = bienesServiciosModel.objects.filter(usuario=perfil,estado=True).count()
		context['bienes_servicios_inactivos'] = bienesServiciosModel.objects.filter(usuario=perfil,estado=False).count()

		return context

def inicio(request):
	cantidad_last_update = 5
	context = {
		'last_update' : bienesServiciosModel.objects.all().order_by('-fecha_actualizacion')[:cantidad_last_update],
		'more' : bienesServiciosModel.objects.all().order_by('-fecha_actualizacion')[cantidad_last_update:]
		}
	print(context)
	return render(request,'home.html',context)

def view_404(request):
	return render(request,'404.html')

def view_500(request):
	return render(request,'500.html')

