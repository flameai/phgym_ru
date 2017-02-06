# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

class Oferta(models.Model):
    slug = models.CharField(max_length=255,unique=True)
    content = RichTextField()
    url = models.URLField(default="",blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        self.url = settings.OFERTA_URL + self.slug + "/"
        super(Oferta, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'оферта'
        verbose_name_plural = u'оферты'
