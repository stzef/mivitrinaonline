{% extends "mail_templated/base.tpl" %}

{% block subject %}
	{{ subject }}
{% endblock %}

{% block html %}
	<div style="background-color: #f5f5f5; padding: 40px 20px; text-align: center;">
		<div style="background-color: white; margin: 0 auto; width: 80%; padding: 20px 20px; border-radius: 5px 5px; box-shadow: 1px 4px 19px -15px rgba(0,0,0,0.75);">
			<h1>Hola {{ args.user.first_name }},</h1>
			<p>Hemos recibido una solicitud para restablecer la contraseña de la cuenta {{ args.email }}.</p>
			<p>Simplemente da click sobre el botón Cambiar contraseña</p>
			<a href="{{ protocol }}{{ domain }}{% url 'password_reset_confirm' uidb64=args.uid token=args.token %}" style="background-color: #3498db; padding: 10px 10px; border-radius: 3px 3px; color: white; text-decoration: none;">Cambiar contraseña</a>
			<p>Si no solicitó cambio de contraseña, no se preocupe! Su contraseña sigue siendo segura y puede ignorar este correo electrónico.</p>
			<p>Equipo de MiVitrinaOnline.</p>
		</div>
	</div>
{% endblock %}