from django.db import models
from usuarios.models import perfilUsuarioModel
from django.template import defaultfilters


HABILIDADES_FOTO_DEFAULT = 'habilidades/img/no_image.png'

class habCategoriasModelManager(models.Manager):
	def get_by_natural_key(self, categoria):
		return self.get(categoria=categoria)

class habCategoriasModel(models.Model):
	categoria = models.CharField(max_length=30,blank=False,null=False)
	slug = models.CharField(unique=True,max_length=30,blank=False,null=False)
	objects = habCategoriasModelManager()

	def __str__(self):
		return u'%s' % (self.categoria)

	def __unicode__(self):
		return u'%s' % (self.categoria)

	def natural_key(self):
		return (self.categoria)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.categoria)
		super(habCategoriasModel, self).save( *args, **kwargs)

class habilidadesModel(models.Model):
	usuario = models.ForeignKey(perfilUsuarioModel)
	categoria = models.ForeignKey(habCategoriasModel)
	nhabilidad = models.CharField(max_length=50,blank=False,null=False)
	slug = models.SlugField(unique=True,max_length=50,editable=False)
	descripcion = models.CharField(max_length=250,blank=False,null=False)
	foto = models.ImageField(upload_to= 'habilidades/img',blank=True,null=True, default=HABILIDADES_FOTO_DEFAULT)
	val_promedio = models.IntegerField(blank=True,null=True)
	num_solicitudes = models.IntegerField(blank=True,null=True,default=0)
	estado = models.BooleanField(default=True)
	precio = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
	fecha_creacion =  models.DateTimeField(auto_now=True,null=False,blank=True)

	def __str__(self):
		return u'%s' % (self.nhabilidad)

	def __unicode__(self):
		return u'%s' % (self.nhabilidad)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nhabilidad)
		super(habilidadesModel, self).save( *args, **kwargs)

