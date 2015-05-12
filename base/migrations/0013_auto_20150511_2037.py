# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_project_face_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='sale',
            field=models.BooleanField(help_text='Указать отображение на главной странице', default=True, verbose_name='Акция'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='name',
            field=models.CharField(unique=True, max_length=50, verbose_name='Название'),
        ),
    ]
