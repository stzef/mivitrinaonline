# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        ('habilidades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='habilidadesmodel',
            name='usuario',
            field=models.ForeignKey(to='usuarios.perfilUsuarioModel'),
            preserve_default=True,
        ),
    ]
