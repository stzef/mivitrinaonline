# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-08-16 04:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bienes_servicios', '0004_comentariosbienesserviciosmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariosbienesserviciosmodel',
            name='comentario',
            field=models.CharField(max_length=2000),
        ),
    ]
