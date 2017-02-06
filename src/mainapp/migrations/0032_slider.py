# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-30 12:54
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_auto_20161124_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Рисунок')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('context', ckeditor.fields.RichTextField(verbose_name='Текст')),
                ('button_url', models.URLField(verbose_name='Ссылка кнопки')),
                ('button_text', models.CharField(max_length=100, verbose_name='Текст на кнопке')),
            ],
            options={
                'verbose_name_plural': 'слайдеры',
                'verbose_name': 'слайдер',
            },
        ),
    ]
