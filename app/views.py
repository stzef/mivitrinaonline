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
		context['habilidades_activas'] = bienesServiciosModel.objects.filter(usuario=perfil,estado=True).count()
		context['habilidades_inactivas'] = bienesServiciosModel.objects.filter(usuario=perfil,estado=False).count()

		return context




def inicio(request):
	return render(request,'home.html')

def view_404(request):
	return render(request,'404.html')

def view_500(request):
	return render(request,'500.html')

