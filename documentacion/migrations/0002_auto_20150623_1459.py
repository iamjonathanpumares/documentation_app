# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='modulo_depende',
            field=models.ForeignKey(related_name='submodulos', blank=True, to='documentacion.Modulo', null=True),
        ),
    ]
