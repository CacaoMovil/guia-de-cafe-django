# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0004_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='logo',
            field=models.ImageField(help_text=b'Formato PNG transparente y 512x512 pixels de tama\xc3\xb1o', upload_to=b'cacao/', verbose_name=b'Imagen'),
            preserve_default=True,
        ),
    ]
