# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0024_auto_20160608_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='last_deal',
            field=models.DateField(verbose_name='Время заказа'),
        ),
    ]
