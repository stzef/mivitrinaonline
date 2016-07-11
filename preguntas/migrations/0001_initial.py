# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respuestas', '__first__'),
        ('habilidades', '0002_habilidadesmodel_usuario'),
        ('usuarios', '0002_auto_20150711_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='preguntasModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pregunta', models.CharField(max_length=1000)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('estado', models.BooleanField(default=True)),
                ('habilidad', models.ForeignKey(to='habilidades.habilidadesModel')),
                ('ofertante', models.ForeignKey(related_name=b'ofertante', to='usuarios.perfilUsuarioModel')),
                ('respuesta', models.ForeignKey(blank=True, to='respuestas.respuestasModel', null=True)),
                ('solicitante', models.ForeignKey(related_name=b'solicitante', to='usuarios.perfilUsuarioModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
