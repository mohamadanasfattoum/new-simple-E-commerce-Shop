# Generated by Django 5.2.1 on 2025-05-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0004_alter_stock_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name="Stock",
        ),
    ]
