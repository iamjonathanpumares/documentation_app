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
                ('nivel', models.PositiveSmallIntegerField(verbose_name=b'Nivel del m\xc3\xb3dulo')),
                ('path', models.CharField(max_length=250, verbose_name=b'Ruta del m\xc3\xb3dulo')),
                ('modulo_depende', models.ForeignKey(related_name='submodulos', blank=True, to='documentacion.Modulo', null=True)),
                ('modulo_principal', models.ForeignKey(related_name='submodulos_totales', blank=True, to='documentacion.Modulo', null=True)),
                ('proyecto', models.ForeignKey(related_name='modulos', to='proyectos.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre_paquete', models.CharField(max_length=35, verbose_name=b'Nombre del paquete')),
                ('descripcion_paquete', models.TextField(verbose_name=b'Descripci\xc3\xb3n del paquete (opcional)', blank=True)),
                ('path', models.CharField(max_length=250, verbose_name=b'Ruta del paquete', blank=True)),
                ('modulo', models.ForeignKey(related_name='paquetes', blank=True, to='documentacion.Modulo', null=True)),
                ('paquetes_requeridos', models.ManyToManyField(related_name='paquetes_dependen', to='documentacion.Paquete')),
                ('proyecto', models.ForeignKey(related_name='paquetes', to='proyectos.Proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='TipoPaquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clave_paquete', models.CharField(unique=True, max_length=5, verbose_name=b'Clave del paquete')),
                ('tipo_paquete', models.CharField(max_length=50, verbose_name=b'Tipo del paquete')),
            ],
        ),
        migrations.AddField(
            model_name='paquete',
            name='tipo_paquete',
            field=models.ForeignKey(related_name='paquetes', to='documentacion.TipoPaquete'),
        ),
    ]
