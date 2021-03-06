# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-11 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0003_auto_20170811_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soda',
            name='brand',
            field=models.CharField(help_text='Название бренда', max_length=100),
        ),
        migrations.AlterField(
            model_name='soda',
            name='img',
            field=models.ImageField(blank=True, help_text='Изображение', upload_to=''),
        ),
        migrations.AlterField(
            model_name='soda',
            name='tara',
            field=models.CharField(help_text='Материал бутылки', max_length=100),
        ),
        migrations.AlterField(
            model_name='soda',
            name='taste',
            field=models.CharField(help_text='Вкус', max_length=100),
        ),
        migrations.AlterField(
            model_name='soda',
            name='volume',
            field=models.DecimalField(decimal_places=2, help_text='Объем бутылки', max_digits=4),
        ),
    ]
