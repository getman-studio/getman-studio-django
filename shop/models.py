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

class Item(models.Model):
    name = models.CharField(max_length=35)
    description = models.TextField()
    image = models.ImageField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Штука'
        verbose_name_plural = u'Штуки'

    def __unicode__(self):
        return self.name
