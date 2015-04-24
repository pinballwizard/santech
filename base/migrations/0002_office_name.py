# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='office',
            name='name',
            field=models.CharField(verbose_name='Название компании', default=1, max_length=100),
            preserve_default=False,
        ),
    ]
