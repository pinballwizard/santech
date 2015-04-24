# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_office_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='grade',
            field=models.IntegerField(default=5, verbose_name='Оценка'),
            preserve_default=False,
        ),
    ]
