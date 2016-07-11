# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preguntas', '0002_auto_20150824_1447'),
        ('respuestas', '0002_auto_20150813_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='respuestasmodel',
            name='pregunta',
            field=models.OneToOneField(null=True, blank=True, to='preguntas.preguntasModel'),
            preserve_default=True,
        ),
    ]
