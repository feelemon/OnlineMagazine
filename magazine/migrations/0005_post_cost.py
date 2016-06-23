# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20160605_0729'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cost',
            field=models.IntegerField(default=123),
            preserve_default=False,
        ),
    ]
