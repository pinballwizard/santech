# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_auto_20150429_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='face_image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Заставка'),
            preserve_default=False,
        ),
    ]
