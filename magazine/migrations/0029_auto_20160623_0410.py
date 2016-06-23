# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0028_auto_20160623_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_add',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 23, 1, 10, 27, 476459, tzinfo=utc)),
        ),
    ]
