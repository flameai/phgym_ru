# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-24 10:42
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0075_auto_20170421_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='title_internal',
            field=models.CharField(default='\u0421\u043b\u0430\u0439\u0434\u0435\u0440', help_text='\u041e\u0442\u043e\u0431\u0440\u0430\u0436\u0430\u0435\u0442\u0441\u044f \u0442\u043e\u043b\u044c\u043a\u043e \u0432 \u0430\u0434\u043c.\u0447\u0430\u0441\u0442\u0438', max_length=200, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slider',
            name='button_text',
            field=models.CharField(blank=True, help_text='\u0415\u0441\u043b\u0438 \u043d\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0434\u043b\u044f \u043a\u043d\u043e\u043f\u043a\u0438, \u0442\u043e \u0432\u0435\u0441\u044c \u0441\u043b\u0430\u0439\u0434\u0435\u0440 \u0431\u0443\u0434\u0435\u0442 \u0441\u0441\u044b\u043b\u043a\u043e\u0439', max_length=100, verbose_name='\u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='context',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='\u0422\u0435\u043a\u0441\u0442'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=b'', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='subtitle',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u041f\u043e\u0434\u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a'),
        ),
    ]
