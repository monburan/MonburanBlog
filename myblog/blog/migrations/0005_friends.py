# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160820_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe5\x8f\x8b\xe6\x83\x85\xe9\x93\xbe\xe6\x8e\xa5')),
            ],
        ),
    ]
