# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20150427_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], verbose_name='Оценка'),
        ),
    ]
