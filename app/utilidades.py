from django.core.exceptions import ObjectDoesNotExist


#Limpia el key 'Model' retornado por el serializador de Modelos
def cleanJsonModel(data):
	for d in data:
		del d['model']
	return data

#Retorna un objeto de un modelo si exite si no retorna None

def get_or_none(Model, **kwargs):
	try:
		return Model.objects.get(**kwargs)
	except ObjectDoesNotExist:
		return None