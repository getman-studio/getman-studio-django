# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 20:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
            options={
                'verbose_name': '\u0428\u0442\u0443\u043a\u0430',
                'verbose_name_plural': '\u0428\u0442\u0443\u043a\u0438',
            },
        ),
    ]