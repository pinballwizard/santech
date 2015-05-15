# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20150515_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Описание'),
        ),
    ]
