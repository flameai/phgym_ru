# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-08 08:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0045_auto_20170207_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='club',
        ),
        migrations.RemoveField(
            model_name='news',
            name='main_photo',
        ),
        migrations.RemoveField(
            model_name='news',
            name='text',
        ),
        migrations.AddField(
            model_name='news',
            name='full_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'', verbose_name='\u043f\u043e\u043b\u043d\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
        migrations.AddField(
            model_name='news',
            name='short_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=b'', verbose_name='\u043a\u0440\u0430\u0442\u043a\u0438\u0439 \u0442\u0435\u043a\u0441\u0442 \u043d\u043e\u0432\u043e\u0441\u0442\u0438'),
        ),
    ]
