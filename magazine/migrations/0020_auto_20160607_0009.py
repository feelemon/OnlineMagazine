# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0019_auto_20160607_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_deal',
            field=models.DateField(default=datetime.datetime(2016, 6, 7, 0, 9, 24, 257510), verbose_name='Время заказа'),
        ),
    ]
