# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20150515_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partner',
            options={'verbose_name_plural': 'Партнеры', 'verbose_name': 'Партнер'},
        ),
        migrations.AddField(
            model_name='socialwidget',
            name='office',
            field=models.ForeignKey(default=1, to='base.Office', blank=True),
            preserve_default=False,
        ),
    ]
