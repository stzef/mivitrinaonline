# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='perfilUsuarioModel',
            fields=[
                ('usuario', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cedula', models.IntegerField(max_length=20, null=True, blank=True)),
                ('genero', models.CharField(default=b'Masculino', max_length=15, choices=[(b'M', b'Masculino'), (b'F', b'Femenino'), (b'O', b'Otro')])),
                ('fnacimiento', models.DateField(null=True, blank=True)),
                ('foto', models.ImageField(default=b'usuarios/avatar/user.jpg', null=True, upload_to=b'usuarios/avatar/', blank=True)),
                ('celular1', models.IntegerField(max_length=15, null=True, blank=True)),
                ('celular2', models.IntegerField(max_length=15, null=True, blank=True)),
                ('celular3', models.IntegerField(max_length=15, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
