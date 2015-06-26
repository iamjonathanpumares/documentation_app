# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('procesos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividad',
            name='nombre_actividad',
            field=models.CharField(max_length=150, verbose_name=b'Nombre de la actividad'),
        ),
    ]
