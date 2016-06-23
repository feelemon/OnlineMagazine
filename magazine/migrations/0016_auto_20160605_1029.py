# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0015_auto_20160605_1027'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Backet',
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Товары', 'verbose_name': 'Товар'},
        ),
    ]
