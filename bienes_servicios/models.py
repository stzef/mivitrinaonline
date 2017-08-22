from django.db import models
from usuarios.models import perfilUsuarioModel
from django.template import defaultfilters
from django.contrib.auth.models import User

BIEN_SERVICIO_FOTO_DEFAULT = 'bienes_servicios/img/no_image.png'

class categoriasModelManager(models.Manager):
	def get_by_natural_key(self, categoria):
		return self.get(categoria=categoria)

class categoriasModel(models.Model):
	categoria = models.CharField(max_length=30,blank=False,null=False)
	slug = models.CharField(unique=True,max_length=30,blank=False,null=False)
	objects = categoriasModelManager()

	def __str__(self):
		return u'%s' % (self.categoria)

	def __unicode__(self):
		return u'%s' % (self.categoria)

	def natural_key(self):
		return (self.categoria)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.categoria)
		super(categoriasModel, self).save( *args, **kwargs)

class bienesServiciosModel(models.Model):
	usuario = models.ForeignKey(perfilUsuarioModel)
	categoria = models.ForeignKey(categoriasModel)
	nBienServicio = models.CharField(max_length=50,blank=False,null=False)
	slug = models.SlugField(unique=True,max_length=50,editable=False)
	descripcion = models.CharField(max_length=250,blank=False,null=False)
	foto = models.ImageField(upload_to= 'bienes_servicios/img',blank=True,null=True, default=BIEN_SERVICIO_FOTO_DEFAULT)
	val_promedio = models.IntegerField(blank=True,null=True)
	num_solicitudes = models.IntegerField(blank=True,null=True,default=0)
	estado = models.BooleanField(default=True)
	precio = models.DecimalField(max_digits=12,decimal_places=2,blank=True,null=True)
	fecha_creacion = models.DateTimeField(auto_now=True,null=False,blank=True)
	fecha_actualizacion = models.DateTimeField(auto_now=True,null=False,blank=True)
	numero_visita = models.IntegerField(default = 0)

	def __str__(self):
		return u'%s' % (self.nBienServicio)

	def __unicode__(self):
		return u'%s' % (self.nBienServicio)

	def save(self, *args, **kwargs):
		self.slug = defaultfilters.slugify(self.nBienServicio)
		super(bienesServiciosModel, self).save( *args, **kwargs)

class comentariosBienesServiciosModel(models.Model):
	usuario = models.ForeignKey(User)
	bienServicio = models.ForeignKey(bienesServiciosModel)
	comentario = models.CharField(max_length=2000)