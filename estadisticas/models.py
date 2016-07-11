from django.db import models

from habilidades.models import habilidadesModel
from usuarios.models import perfilUsuarioModel

class habilidadesSolicitadasModel(models.Model):
	habilidad = models.ForeignKey(habilidadesModel)
	usuario = models.ForeignKey(perfilUsuarioModel, null=True, blank=True)
	fecha = models.DateTimeField(auto_now=True, null=False, blank=False)

	def __str__(self):
		return u'%s' % (self.habilidad)

	def __unicode__(self):
		return u'%s' % (self.habilidad)