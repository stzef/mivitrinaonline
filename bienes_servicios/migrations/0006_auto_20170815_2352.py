# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-08-16 04:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bienes_servicios', '0005_auto_20170815_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentariosbienesserviciosmodel',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
