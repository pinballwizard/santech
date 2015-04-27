# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20150427_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.IntegerField(default=5, verbose_name='Оценка', choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
    ]
