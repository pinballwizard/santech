# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_blog_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='phone_str',
        ),
        migrations.AddField(
            model_name='office',
            name='maptype',
            field=models.CharField(max_length=30, choices=[('yandex#map', 'Схема'), ('yandex#satellite', 'Спутник'), ('yandex#hybrid', 'Гибрид'), ('yandex#publicMap', 'Народная'), ('yandex#publicMapHybrid', 'Народная+Гибрид')], verbose_name='Тип карты', default='yandex#map'),
        ),
        migrations.AddField(
            model_name='office',
            name='phone1',
            field=models.CharField(max_length=15, verbose_name='Телефон Офис', blank=True),
        ),
        migrations.AddField(
            model_name='office',
            name='phone2',
            field=models.CharField(max_length=15, verbose_name='Телефон Тех.поддержки', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blog', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='carouselimage',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Подпись', blank=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='email',
            field=models.EmailField(max_length=50, verbose_name='Контактная почта', blank=True),
        ),
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to='partner', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(upload_to='service', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='photo',
            field=models.ImageField(upload_to='worker', verbose_name='Фотография'),
        ),
    ]
