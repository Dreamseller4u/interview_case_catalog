# Generated by Django 4.1 on 2022-08-19 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_remove_sales_procent discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='discount',
            field=models.IntegerField(default=10),
        ),
    ]