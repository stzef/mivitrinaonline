# -*- encoding: utf-8 -*-
from django import forms
from models import bienesServiciosModel

class nuevaHabilidadForm(forms.ModelForm):
	class Meta:
		model = bienesServiciosModel
		fields = ['categoria','nBienServicio','descripcion','precio']
		widgets = {
			'categoria':forms.Select(attrs={'class':'form-control','required':''}),
			'nBienServicio': forms.TextInput(attrs={'class': 'form-control','placeholder':'Cual es tu bien/servicio','required':''}),
			'descripcion': forms.Textarea(attrs={'rows': 2, 'class':'form-control','placeholder':'Describe tu bien/servicio','required':''}),
			'precio': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
		}
		
		labels = {
			'categoria': ('Categoria'),
			'nBienServicio': ('Bien/Servicios'),
		}
