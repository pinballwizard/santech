# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_auto_20150515_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='partner', verbose_name='Логотип')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
            ],
            options={
                'verbose_name_plural': 'Партнера',
                'verbose_name': 'Партнер',
            },
        ),
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name_plural': 'Новости', 'verbose_name': 'Новость'},
        ),
        migrations.AlterModelOptions(
            name='mail',
            options={'verbose_name_plural': 'Письма', 'verbose_name': 'Письмо'},
        ),
        migrations.AlterModelOptions(
            name='office',
            options={'verbose_name_plural': 'Офис', 'verbose_name': 'Офисы'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'verbose_name_plural': 'Цены', 'verbose_name': 'Цена'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': 'Проекты', 'verbose_name': 'Проект'},
        ),
        migrations.AlterModelOptions(
            name='projectimage',
            options={'verbose_name_plural': 'Фотографии проекта', 'verbose_name': 'Фотография проекта'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Отзывы', 'verbose_name': 'Отзыв'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name_plural': 'Услуги', 'verbose_name': 'Услуга'},
        ),
        migrations.AlterModelOptions(
            name='socialwidget',
            options={'verbose_name_plural': 'Социальные виджеты', 'verbose_name': 'Социальный виджет'},
        ),
        migrations.AlterModelOptions(
            name='worker',
            options={'verbose_name_plural': 'Работники', 'verbose_name': 'Работник'},
        ),
    ]
