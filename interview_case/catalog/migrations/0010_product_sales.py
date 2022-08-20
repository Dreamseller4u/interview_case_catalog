# Generated by Django 4.1 on 2022-08-19 13:11

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_remove_product_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales',
            field=mptt.fields.TreeForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.sales'),
        ),
    ]