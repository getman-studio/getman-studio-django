# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=15)
    text_id = models.SlugField(max_length=15)

    class Meta:
        verbose_name = u'Категорія'
        verbose_name_plural = u'Категорії'

    def __unicode__(self):
       return self.name


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery/")
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u'Елемент галереї'
        verbose_name_plural = u'Елементи галереї'

    def __unicode__(self):
        return self.category.name + ": " + self.description

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    text_id = models.SlugField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    image1 = models.ImageField(upload_to="workshop/")
    image2 = models.ImageField(upload_to="workshop/", null=True, blank=True)
    author = models.CharField(max_length=255)

    class Meta:
        verbose_name = u'Новина'
        verbose_name_plural = u'Новини'

    def __unicode__(self):
        return self.name


class WorkshopParallaxItem(models.Model):
    image = models.ImageField(upload_to="parallax/")

    class Meta:
        verbose_name = u'Картинка параллаксу'
        verbose_name_plural = u'Картинки параллаксу'

    def __unicode__(self):
        return u"Картинка в параллаксі"
