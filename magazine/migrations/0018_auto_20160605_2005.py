# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0017_auto_20160605_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_deal',
            field=models.DateField(default=datetime.datetime(2016, 6, 5, 20, 5, 35, 936355), verbose_name='Время заказа'),
        ),
    ]
