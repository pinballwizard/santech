# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=20, unique=True)),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='')),
                ('text', models.TextField(verbose_name='Текст', max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(verbose_name='Картинка', upload_to='carousel')),
                ('text', models.CharField(verbose_name='Подпись', max_length=100)),
                ('position', models.IntegerField(verbose_name='Позиция', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sender', models.CharField(verbose_name='Отправитель', max_length=30)),
                ('email', models.EmailField(verbose_name='Email', max_length=30)),
                ('subject', models.CharField(verbose_name='Тема', max_length=50)),
                ('message', models.TextField(verbose_name='Сообщение', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('address', models.CharField(verbose_name='Контактный адресс', max_length=100)),
                ('email', models.EmailField(verbose_name='Контактная почта', max_length=50)),
                ('phone_str', models.CharField(verbose_name='Контактный телефон (через ;)', max_length=100)),
                ('latitude', models.CharField(verbose_name='Широта', max_length=10)),
                ('longitude', models.CharField(verbose_name='Долгота', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=20, unique=True)),
                ('logo', models.ImageField(verbose_name='Логотип', upload_to='')),
                ('url', models.URLField(verbose_name='Ссылка на сайт')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Название', max_length=30)),
                ('price', models.IntegerField(verbose_name='Цена')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('owner', models.CharField(verbose_name='Клиент', max_length=50, unique=True)),
                ('header', models.CharField(verbose_name='Заголовок', max_length=20)),
                ('text', models.CharField(verbose_name='Отзыв', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('image', models.ImageField(verbose_name='Изображение', upload_to='')),
                ('header', models.CharField(verbose_name='Заголовок', max_length=100)),
                ('text', models.TextField(verbose_name='Описание', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='SocialWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(choices=[('vk', 'Вконтакте'), ('ok', 'Одноклассники'), ('fb', 'Facebook'), ('tw', 'Twitter'), ('li', 'LinkedIn'), ('yt', 'YouTube'), ('in', 'Instagram')], verbose_name='Название', max_length=2)),
                ('url', models.URLField(blank=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(verbose_name='Имя', max_length=30)),
                ('last_name', models.CharField(verbose_name='Фамилия', max_length=30)),
                ('birth_day', models.DateField(verbose_name='День рождения')),
                ('email', models.EmailField(verbose_name='Почта', max_length=254)),
                ('photo', models.ImageField(verbose_name='Фотография', upload_to='')),
                ('phone', models.CharField(verbose_name='Телефон', max_length=100)),
            ],
        ),
    ]
