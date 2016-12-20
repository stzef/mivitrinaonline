# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='bienesServiciosModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nBienServicio', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('descripcion', models.CharField(max_length=250)),
                ('foto', models.ImageField(default=b'bienes_servicios/img/no_image.png', null=True, upload_to=b'bienes_servicios/img', blank=True)),
                ('val_promedio', models.IntegerField(null=True, blank=True)),
                ('num_solicitudes', models.IntegerField(default=0, null=True, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('precio', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='categoriasModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=30)),
                ('slug', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='bienesserviciosmodel',
            name='categoria',
            field=models.ForeignKey(to='bienes_servicios.categoriasModel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='bienesserviciosmodel',
            name='usuario',
            field=models.ForeignKey(to='usuarios.perfilUsuarioModel'),
            preserve_default=True,
        ),
    ]
