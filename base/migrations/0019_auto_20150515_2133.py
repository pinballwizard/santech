# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20150515_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectimage',
            name='header',
        ),
        migrations.AddField(
            model_name='office',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Метаописание сайта'),
        ),
        migrations.AddField(
            model_name='office',
            name='keywords',
            field=models.TextField(blank=True, max_length=200, verbose_name='Ключевые слова для поиска'),
        ),
    ]
