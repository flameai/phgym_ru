# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-06 02:15
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0096_auto_20180212_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitneszone',
            name='short_description',
            field=models.CharField(default=b'', max_length=195, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435'),
        ),
        migrations.AddField(
            model_name='stock',
            name='feedback_code',
            field=models.TextField(blank=True, default=b'\n<a class="flamp-widget" href="//moscow.flamp.ru/firm/panaekhali_kafe_bar-4504127908393518"  data-flamp-widget-type="responsive-new" data-flamp-widget-id="4504127908393518" data-flamp-widget-width="100%" data-flamp-widget-count="1">\xd0\x9e\xd1\x82\xd0\xb7\xd1\x8b\xd0\xb2\xd1\x8b \xd0\xbe \xd0\xbd\xd0\xb0\xd1\x81 \xd0\xbd\xd0\xb0 \xd0\xa4\xd0\xbb\xd0\xb0\xd0\xbc\xd0\xbf\xd0\xb5</a><script>!function(d,s){var js,fjs=d.getElementsByTagName(s)[0];js=d.createElement(s);js.async=1;js.src="//widget.flamp.ru/loader.js";fjs.parentNode.insertBefore(js,fjs);}(document,"script");</script>', null=True, verbose_name='\u041a\u043e\u0434 \u043e\u0442\u0437\u044b\u0432\u043e\u0432'),
        ),
        migrations.AddField(
            model_name='stock',
            name='feedback_enabled',
            field=models.BooleanField(default=True, verbose_name='\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u043e\u0442\u0437\u044b\u0432\u044b \u043d\u0430 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0435'),
        ),
        migrations.AddField(
            model_name='stock',
            name='pricing',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=b'\n<div class="col-md-12 col-md-3">\n    <div class="conditions__time">\n        <div class="conditions__text">\n            \xd0\x97\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd1\x8f \xd0\xb1\xd1\x83\xd0\xb4\xd1\x83\xd1\x82 \xd0\xbf\xd1\x80\xd0\xbe\xd1\x85\xd0\xbe\xd0\xb4\xd0\xb8\xd1\x82\xd1\x8c \xd0\xbf\xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbd\xd0\xb5\xd0\xb4\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbc \xd0\xb8 \xd1\x81\xd1\x80\xd0\xb5\xd0\xb4\xd0\xb0\xd0\xbc \xd0\xb2 00:00\n        </div>\n    </div>\n</div>\n<div class="col-md-12 col-md-9">\n    <div class="conditions__item col-xs-12 col-sm-6 col-md-6">\n        <div class="conditions__text col-md-4">\n            \xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd1\x8f\n        </div>\n\n        <div class="conditions__cost col-md-8">\n            <div class="conditions__price">000 \xd1\x80\xd1\x83\xd0\xb1</div>\n        </div>\n    </div>\n    <div class="conditions__item col-xs-12 col-sm-6 col-md-6">\n        <div class="conditions__text col-md-4">\n            \xd0\x91\xd0\xbb\xd0\xbe\xd0\xba \xd0\xb8\xd0\xb7 0 \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb9\n        </div>\n\n        <div class="conditions__cost col-md-8">\n            <div class="conditions__price">00 000 \xd1\x80\xd1\x83\xd0\xb1</div>\n            <div class="conditions__saving">\n                <div class="conditions__saving-value">000 \xd1\x80\xd1\x83\xd0\xb1</div>\n                <div class="conditions__saving-text">\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb8\xd1\x8f</div>\n            </div>\n        </div>\n    </div>\n    <div class="conditions__item col-xs-12 col-sm-6 col-md-6">\n        <div class="conditions__text col-md-4">\n            \xd0\xa1\xd1\x82\xd0\xbe\xd0\xb8\xd0\xbc\xd0\xbe\xd1\x81\xd1\x82\xd1\x8c \xd0\xbe\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd1\x8f\n        </div>\n\n        <div class="conditions__cost col-md-8">\n            <div class="conditions__price">000 \xd1\x80\xd1\x83\xd0\xb1</div>\n        </div>\n    </div>\n    <div class="conditions__item col-xs-12 col-sm-6 col-md-6">\n        <div class="conditions__text col-md-4">\n            \xd0\x91\xd0\xbb\xd0\xbe\xd0\xba \xd0\xb8\xd0\xb7 0 \xd0\xb7\xd0\xb0\xd0\xbd\xd1\x8f\xd1\x82\xd0\xb8\xd0\xb9\n        </div>\n\n        <div class="conditions__cost col-md-8">\n            <div class="conditions__price">00 000 \xd1\x80\xd1\x83\xd0\xb1</div>\n            <div class="conditions__saving">\n                <div class="conditions__saving-value">000 \xd1\x80\xd1\x83\xd0\xb1</div>\n                <div class="conditions__saving-text">\xd0\xad\xd0\xba\xd0\xbe\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb8\xd1\x8f</div>\n            </div>\n        </div>\n    </div>\n</div>\n', null=True, verbose_name='\u0426\u0435\u043d\u044b'),
        ),
        migrations.AddField(
            model_name='stock',
            name='top_action_image',
            field=models.ImageField(blank=True, default=b'', null=True, upload_to=b'', verbose_name='\u0412\u0435\u0440\u0445\u043d\u0438\u0435\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0410\u043a\u0446\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='stock',
            name='top_action_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='\u0412\u0435\u0440\u0445\u043d\u0435\u0435 \u043a\u043e\u0440\u043e\u0442\u043a\u043e\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0430\u043a\u0446\u0438\u0438'),
        ),
        migrations.AddField(
            model_name='stock',
            name='top_action_title',
            field=models.CharField(blank=True, max_length=65, null=True, verbose_name='\u0412\u0435\u0440\u0445\u043d\u0438\u0439 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0410\u043a\u0446\u0438\u0438'),
        ),
    ]
