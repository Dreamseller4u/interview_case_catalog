# Generated by Django 4.1 on 2022-08-19 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_product_sales'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sales',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
