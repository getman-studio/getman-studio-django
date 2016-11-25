# -*- coding: utf-8 -*-
from django.db import models

class Category(models.Model):
    text_id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)

    def __unicode__(self):
       return self.name


class GalleryItem(models.Model):
    image = models.ImageField(upload_to="gallery/")
    description = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.category.name + self.description

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    text_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()
    image1 = models.ImageField(upload_to="workshop/")
    image2 = models.ImageField(upload_to="workshop/", null=True, blank=True)
    author = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class WorkshopParallaxItem(models.Model):
    image = models.ImageField(upload_to="parallax/")

    def __unicode__(self):
        return u"Картинка в параллаксі"
