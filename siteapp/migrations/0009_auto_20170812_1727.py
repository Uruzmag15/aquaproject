# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-12 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteapp', '0008_auto_20170811_2334'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Brand name.', max_length=100, verbose_name='Бренд')),
                ('descr', models.TextField(blank=True, help_text='Информация о бренде.', verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, help_text='Выберите файл с изображением логотипа.', upload_to='', verbose_name='Логотип')),
            ],
            options={
                'verbose_name_plural': 'brand',
                'verbose_name': 'brand',
            },
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tara', models.CharField(help_text='Материал бутылки.', max_length=100, verbose_name='Тара')),
                ('volume', models.DecimalField(decimal_places=2, help_text='Объем бутылки, л.', max_digits=4, verbose_name='Объем')),
                ('taste', models.CharField(help_text='Вкус.', max_length=100, verbose_name='Вкус')),
                ('photo', models.ImageField(blank=True, help_text='Выберите файл с изображением.', upload_to='', verbose_name='Фото')),
                ('brand', models.ForeignKey(help_text='Название бренда.', on_delete=django.db.models.deletion.CASCADE, to='siteapp.Brand', verbose_name='brand')),
            ],
            options={
                'verbose_name_plural': 'drink',
                'verbose_name': 'drink',
            },
        ),
        migrations.DeleteModel(
            name='Soda',
        ),
    ]
