# Generated by Django 2.0 on 2017-12-03 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]