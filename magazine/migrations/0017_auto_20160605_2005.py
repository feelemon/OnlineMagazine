# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0016_auto_20160605_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cost',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_buy',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='metod',
        ),
        migrations.AddField(
            model_name='order',
            name='last_deal',
            field=models.DateField(verbose_name='Время заказа', default=datetime.datetime(2016, 6, 5, 20, 4, 53, 927571)),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(verbose_name='Имя заказчика', default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='order',
            field=models.CharField(verbose_name='Что заказали', default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(verbose_name='Телефон заказчика', default=12, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='sum',
            field=models.IntegerField(verbose_name='Сумма заказа', default=0),
        ),
    ]
