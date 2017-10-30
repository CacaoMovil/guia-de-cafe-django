# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cacao', '0013_auto_20151202_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['guide__number', 'peso'], 'verbose_name': 'Seccion', 'verbose_name_plural': 'Secciones'},
        ),
    ]
