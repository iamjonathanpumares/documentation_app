# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_modulo', models.CharField(max_length=35, verbose_name=b'Nombre del m\xc3\xb3dulo')),
                ('descripcion_modulo', models.TextField(verbose_name=b'Descripci\xc3\xb3n del m\xc3\xb3dulo')),
                ('proyecto', models.ForeignKey(related_name='modulos', to='proyectos.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_paquete', models.CharField(max_length=50, verbose_name=b'Nombre del paquete')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPaquete',
            fields=[
                ('clave_paquete', models.CharField(max_length=3, serialize=False, verbose_name=b'Clave del paquete', primary_key=True)),
                ('tipo_paquete', models.CharField(max_length=50, verbose_name=b'Nombre del paquete')),
            ],
        ),
        migrations.AddField(
            model_name='paquete',
            name='tipo_paquete',
            field=models.ForeignKey(related_name='paquetes', to='documentacion.TipoPaquete'),
        ),
    ]
