# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20150429_2026'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImage',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project', verbose_name='Картинка')),
                ('header', models.CharField(max_length=100, blank=True, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=500, blank=True, verbose_name='Комментарий')),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='header',
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project',
            name='text',
        ),
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=100, default=1, verbose_name='Название проекта'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projectimage',
            name='project',
            field=models.ForeignKey(to='base.Project'),
        ),
    ]
