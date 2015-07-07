# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0003_paquete_paquetes_requeridos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulo',
            name='modulo_depende',
        ),
        migrations.AddField(
            model_name='modulo',
            name='modulos_depende',
            field=models.ManyToManyField(related_name='submodulos', to='documentacion.Modulo'),
        ),
    ]
