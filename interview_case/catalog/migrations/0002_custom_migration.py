from django.db import migrations, models


def forwards_func(apps, schema_editor):
    # Функция при миграции находит все продукты привязаные к 1 категории и ставит знак False в поле availible
    Product = apps.get_model("catalog", "Product")
    for product in Product.objects.filter(category_id = 1):
        product.availible = False
        product.save()
    

def reverse_func(apps, schema_editor):
    # Обратная функция при откате миграции находит все продукты привязаные к 1 категории и ставит знак True в поле availible
    Product = apps.get_model("catalog", "Product")
    for product in Product.objects.filter(category_id = 1):
        product.availble = True
        product.save()

class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
