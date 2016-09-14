# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe5\x85\xb3\xe4\xba\x8e\xe6\x88\x91')),
            ],
            options={
                'verbose_name': '\u5173\u4e8e\u6211',
                'verbose_name_plural': '\u5173\u4e8e\u6211',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('author', models.CharField(max_length=16, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85')),
                ('summary', models.CharField(max_length=50, verbose_name=b'\xe6\x91\x98\xe8\xa6\x81')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe6\xad\xa3\xe6\x96\x87')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('status', models.CharField(max_length=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(b'p', b'\xe5\xb7\xb2\xe5\x8f\x91\xe5\xb8\x83'), (b'w', b'\xe8\x8d\x89\xe7\xa8\xbf')])),
            ],
            options={
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', ckeditor.fields.RichTextField(verbose_name=b'\xe5\xa5\xbd\xe5\x8f\x8b')),
            ],
            options={
                'verbose_name': '\u597d\u53cb',
                'verbose_name_plural': '\u597d\u53cb',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
