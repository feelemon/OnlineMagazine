# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0027_auto_20160622_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 21, 14, 46, 742747, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.CharField(max_length=200, verbose_name='Цена'),
        ),
    ]
