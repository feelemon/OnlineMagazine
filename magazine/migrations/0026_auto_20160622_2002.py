# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('magazine', '0025_auto_20160608_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('time_add', models.DateTimeField(default=datetime.datetime(2016, 6, 22, 17, 2, 24, 327378, tzinfo=utc))),
                ('col', models.IntegerField(default=1)),
                ('item', models.ForeignKey(to='magazine.Post')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='sum',
        ),
        migrations.AddField(
            model_name='order',
            name='owner',
            field=models.ForeignKey(default=123, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.ForeignKey(to='magazine.Order'),
        ),
    ]
