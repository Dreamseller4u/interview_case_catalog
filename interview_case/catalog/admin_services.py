from unicodedata import category
from .models import  Sales, Categories, Product
from django.contrib.admin.helpers import ActionForm
from django import forms
from math import ceil
from django.utils.html import format_html



class UpdateActionForm(ActionForm):
    ''' Добавлем в поле выбора скидки из модели Sales'''
    sales = Sales.objects.all()
    params = [('','')]
    for i in sales:
        params.append((f'{i.discount}', i.title))
    discount = forms.ChoiceField(choices=params, required=False)


def set_discount(modeladmin, request, queryset):
    ''' Метод примениния скидки '''
    discount = request.POST['discount']
    discount = float(discount)
    for product in queryset:
        multiplier = discount / 100
        old_price = float(product.price)
        new_price = ceil(old_price - (old_price * multiplier))
        queryset.update(price=new_price, sales=True, sales_amount=discount)


set_discount.short_description = 'Устоновить акцию на продукт'

def unset_discount(modeladmin, request, queryset):
    ''' Метод удаления  скидки и возврата цены обратно'''
    for product in queryset:
        discount = product.sales_amount
        if(discount > 0):
            old_price = float(product.price)
            new_price = ceil(old_price + (old_price * (discount / 100)))
            queryset.update(price=new_price, sales=False, sales_amount=0)
        
unset_discount.short_description = 'Убрать акцию с продукта'

#Admin category
def title_display(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.title,  # Or whatever you want to put here
        )
title_display.short_description = ('title')