# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20150429_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='carousel')),
                ('header', models.CharField(max_length=100, blank=True, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=500, blank=True, verbose_name='Комментарий')),
            ],
        ),
        migrations.DeleteModel(
            name='CarouselImage',
        ),
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.AlterField(
            model_name='service',
            name='header',
            field=models.CharField(max_length=20, verbose_name='Заголовок', unique=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='text',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]
