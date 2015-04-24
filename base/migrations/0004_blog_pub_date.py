# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_review_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 24, 12, 10, 57, 75113, tzinfo=utc), verbose_name='Время публикации'),
            preserve_default=False,
        ),
    ]
