# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from .models import AuditoriaUser

def log_user(user, accion):
	log = AuditoriaUser(usuario = user, accion = accion)
	log.save()

class authEmailBackend(object):
	def authenticate(self, email=None, password=None):
		try:
			user = User.objects.get(email=email)
			if user.check_password(password):
				return user
		except User.DoesNotExist:
			return None

	def get_user(self, user_id):
		try:
			return User.objects.get(id=user_id)
		except User.DoesNotExist:
			return None
