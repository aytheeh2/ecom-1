# Generated by Django 5.0 on 2024-02-02 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
