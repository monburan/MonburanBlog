# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160819_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(default=datetime.datetime(2016, 8, 19, 9, 44, 22, 140000, tzinfo=utc), max_length=16, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=False,
        ),
    ]
