# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20150515_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text',
            field=models.TextField(max_length=20000, verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='project',
            name='face_image',
            field=models.ImageField(verbose_name='Заставка', upload_to='project'),
        ),
    ]
