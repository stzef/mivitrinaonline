# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('habilidades', '0002_habilidadesmodel_usuario'),
        ('usuarios', '0002_auto_20150711_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='habilidadesSolicitadasModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('habilidad', models.ForeignKey(to='habilidades.habilidadesModel')),
                ('usuario', models.ForeignKey(to='usuarios.perfilUsuarioModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
