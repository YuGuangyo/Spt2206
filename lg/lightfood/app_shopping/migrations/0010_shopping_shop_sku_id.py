# Generated by Django 3.2 on 2022-11-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shopping', '0009_shopping_shop_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='shop_sku_id',
            field=models.FloatField(default=1, max_length=32),
        ),
    ]
