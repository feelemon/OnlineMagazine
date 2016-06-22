# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0021_auto_20160607_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_deal',
            field=models.DateField(verbose_name='Время заказа', default=datetime.datetime(2016, 6, 7, 15, 23, 36, 575145)),
        ),
    ]
