# Generated by Django 4.1.3 on 2023-01-06 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0024_alter_stock_high_alter_stock_low_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
    ]
