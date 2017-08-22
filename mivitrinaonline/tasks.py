from mail_templated import send_mail
from django.conf import settings
from .celery import app

@app.task
def send_email_task(template, email, request, subject, args):
	data = {
		'domain': request,
		'protocol': 'http://',
		'subject': subject,
		'args': args
	}
	return send_mail(template, data, settings.EMAIL_HOST_USER, [email])