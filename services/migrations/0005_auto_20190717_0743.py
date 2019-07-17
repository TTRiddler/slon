# Generated by Django 2.2.2 on 2019-07-17 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20190716_1920'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artclass',
            options={'ordering': ['my_order'], 'verbose_name': 'Кружок', 'verbose_name_plural': 'Кружки'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['my_order'], 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterModelOptions(
            name='specialist',
            options={'ordering': ['my_order'], 'verbose_name': 'Специалист', 'verbose_name_plural': 'Специалисты'},
        ),
        migrations.AddField(
            model_name='artclass',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='service',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
        migrations.AddField(
            model_name='specialist',
            name='my_order',
            field=models.PositiveIntegerField(default=0, verbose_name='Сортировка'),
        ),
    ]
