# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estadisticas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidadessolicitadasmodel',
            name='usuario',
            field=models.ForeignKey(blank=True, to='usuarios.perfilUsuarioModel', null=True),
        ),
    ]
