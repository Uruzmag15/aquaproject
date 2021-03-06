# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-11 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0007_auto_20170811_2254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soda',
            name='brand',
            field=models.CharField(help_text='Название бренда.', max_length=100, verbose_name='Бренд'),
        ),
        migrations.AlterField(
            model_name='soda',
            name='photo',
            field=models.ImageField(blank=True, help_text='Выберите файл с изображением.', upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='soda',
            name='tara',
            field=models.CharField(help_text='Материал бутылки.', max_length=100, verbose_name='Тара'),
        ),
        migrations.AlterField(
            model_name='soda',
            name='taste',
            field=models.CharField(help_text='Вкус.', max_length=100, verbose_name='Вкус'),
        ),
        migrations.AlterField(
            model_name='soda',
            name='volume',
            field=models.DecimalField(decimal_places=2, help_text='Объем бутылки.', max_digits=4, verbose_name='Объем'),
        ),
    ]
