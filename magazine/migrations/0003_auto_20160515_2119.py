# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import magazine.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backet',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('product', models.CharField(verbose_name=magazine.models.Product, max_length=200)),
                ('quantity', models.CharField(verbose_name=magazine.models.Product, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('key_words', models.CharField(max_length=100)),
                ('last_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_order', models.DateField()),
                ('date_buy', models.DateField()),
                ('metod', models.CharField(default='PayPal', max_length=200)),
                ('cost', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=100)),
                ('cost', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('date_register', models.DateTimeField(default=django.utils.timezone.now)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('telephone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('cart_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ManyToManyField(to='magazine.Profile', max_length=200),
        ),
        migrations.AddField(
            model_name='backet',
            name='profile',
            field=models.ManyToManyField(to='magazine.Profile'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ManyToManyField(to='magazine.Profile'),
        ),
    ]
