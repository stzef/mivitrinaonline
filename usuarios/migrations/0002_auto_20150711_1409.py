# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='celular1',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='celular2',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='perfilusuariomodel',
            name='celular3',
            field=models.CharField(max_length=15, null=True, blank=True),
        ),
    ]
