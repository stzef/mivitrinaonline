# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('respuestas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='respuestasmodel',
            old_name='fechas',
            new_name='fecha',
        ),
    ]
