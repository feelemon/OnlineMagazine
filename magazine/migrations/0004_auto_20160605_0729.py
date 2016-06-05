# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20160515_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backet',
            name='profile',
        ),
        migrations.RemoveField(
            model_name='backet',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='nik_name',
            field=models.CharField(max_length=300, verbose_name='nik_name', default=123),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='backet',
            name='product',
            field=models.CharField(max_length=40, verbose_name=magazine.models.Product, default=None),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, blank=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=30, verbose_name='first_name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='second_name'),
        ),
    ]
