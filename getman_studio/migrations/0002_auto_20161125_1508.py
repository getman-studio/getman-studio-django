# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getman_studio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryitem',
            name='link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
