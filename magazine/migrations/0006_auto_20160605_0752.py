# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_post_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.SlugField(default=12, verbose_name='Alias категории'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='alias',
            field=models.SlugField(default=123, verbose_name='Alias товара'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default=123, to='magazine.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название Категории'),
        ),
        migrations.AlterField(
            model_name='post',
            name='cost',
            field=models.IntegerField(verbose_name='Цена', default=0),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название Товара'),
        ),
    ]
