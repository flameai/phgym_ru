# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-07-04 07:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0087_news_hidden'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ('order',), 'verbose_name': '\u0430\u043a\u0446\u0438\u044f', 'verbose_name_plural': '\u0430\u043a\u0446\u0438\u0438'},
        ),
    ]
