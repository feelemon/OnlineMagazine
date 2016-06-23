# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0013_auto_20160605_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Категории', 'verbose_name': 'Категория'},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='price',
            new_name='cost',
        ),
        migrations.AddField(
            model_name='category',
            name='last_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
