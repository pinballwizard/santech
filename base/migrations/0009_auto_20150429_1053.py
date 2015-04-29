# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20150427_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='header',
            field=models.CharField(verbose_name='Заголовок', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(verbose_name='Описание', max_length=1000, blank=True),
        ),
    ]
