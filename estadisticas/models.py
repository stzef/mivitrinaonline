from django.db import models

from bienes_servicios.models import bienesServiciosModel
from usuarios.models import perfilUsuarioModel

class bienesServiciosSolicitadosModel(models.Model):
	bien_servicio = models.ForeignKey(bienesServiciosModel)
	usuario = models.ForeignKey(perfilUsuarioModel, null=True, blank=True)
	fecha = models.DateTimeField(auto_now=True, null=False, blank=False)

	def __str__(self):
		return u'%s' % (self.bien_servicio)

	def __unicode__(self):
		return u'%s' % (self.bien_servicio)
