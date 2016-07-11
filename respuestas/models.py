from django.db import models
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


class respuestasModel(models.Model):

	pregunta = models.OneToOneField('preguntas.preguntasModel',blank=True, null=True)
	respuesta = models.CharField(max_length=1000)
	fecha = models.DateTimeField(auto_now=True)


	def enviar_respuesta_email(self):

		#datos para renderizar template de email
		contextoDeTemplateParaEmail = {
			'usuario_de_respuesta' : self.pregunta.ofertante.usuario.get_full_name() ,
			'pregunta' : self.pregunta,
			'respuesta' : self.respuesta,
		}

		#rederizando template local
		template = render_to_string('respuesta_email_template.html',contextoDeTemplateParaEmail)

		#creando mensaje
		msg = EmailMessage(
			subject = 'Oportunidapp (respuesta)',
			from_email = 'sistematizaref <sistematizaref@gmail.com>',
			to = [self.pregunta.solicitante.usuario.email]
		)

		#template mailchimp
		msg.template_name = 'Respuesta'
		msg.template_content = {
			'std_content00' : template,
		}

		#enviando email
		msg.send()


	def __str__(self):
		return u'%s' % (self.respuesta)

	def __unicode__(self):
		return u'%s' % (self.respuesta)


