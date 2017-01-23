# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15)
    text_id = models.SlugField(max_length=15)
    position = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = u'Категорія'
        verbose_name_plural = u'Категорії'
        ordering = ('position', )

    def __unicode__(self):
       return self.name
