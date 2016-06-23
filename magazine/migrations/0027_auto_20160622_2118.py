# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0026_auto_20160622_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.IntegerField(default=1, verbose_name='Количество'),
        ),
        migrations.AlterField(
            model_name='item',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 22, 18, 18, 25, 680208, tzinfo=utc)),
        ),
    ]
