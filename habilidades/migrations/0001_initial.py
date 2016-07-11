# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='habCategoriasModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categoria', models.CharField(max_length=30)),
                ('slug', models.CharField(unique=True, max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='habilidadesModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nhabilidad', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('descripcion', models.CharField(max_length=250)),
                ('foto', models.ImageField(default=b'habilidades/img/no_image.png', null=True, upload_to=b'habilidades/img', blank=True)),
                ('val_promedio', models.IntegerField(null=True, blank=True)),
                ('num_solicitudes', models.IntegerField(default=0, null=True, blank=True)),
                ('estado', models.BooleanField(default=True)),
                ('precio', models.DecimalField(null=True, max_digits=12, decimal_places=2, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(to='habilidades.habCategoriasModel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
