# Generated by Django 2.2.2 on 2019-07-09 16:53

from django.db import migrations, models
import django.db.models.deletion
import services.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(max_length=250, verbose_name='Title')),
                ('desc', models.CharField(max_length=250, verbose_name='Description')),
                ('keywords', models.CharField(max_length=250, verbose_name='Keywords')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
                ('schedule', models.CharField(max_length=250, verbose_name='График')),
                ('one_lesson_price', models.PositiveIntegerField(verbose_name='Цена одного занятия')),
                ('some_lesson_nmb', models.PositiveIntegerField(verbose_name='Количество занятий')),
                ('some_lesson_price', models.PositiveIntegerField(verbose_name='Цена нескольких занятий')),
                ('text', tinymce.models.HTMLField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Услуга',
                'verbose_name_plural': 'Услуги',
            },
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seo_title', models.CharField(max_length=250, verbose_name='Title')),
                ('desc', models.CharField(max_length=250, verbose_name='Description')),
                ('keywords', models.CharField(max_length=250, verbose_name='Keywords')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Категория услуг',
                'verbose_name_plural': 'Категории услуг',
            },
        ),
        migrations.CreateModel(
            name='ImageInService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=services.models.ImageInService.get_picture_url, verbose_name='Изображение')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='services.Service', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]
