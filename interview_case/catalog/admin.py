from math import ceil
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Product, Categories, Sales
from django.contrib.admin.helpers import ActionForm
from django import forms
from math import ceil


class CategoriesAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Categories, CategoriesAdmin)


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


set_discount.short_description = 'Set discount on products'

def unset_discount(modeladmin, request, queryset):
    ''' Метод удаления  скидки и возврата цены обратно'''
    for product in queryset:
        discount = product.sales_amount
        if(discount > 0):
            old_price = float(product.price)
            new_price = ceil(old_price + (old_price * (discount / 100)))
            queryset.update(price=new_price, sales=False, sales_amount=0)
        
unset_discount.short_description = 'Unset discount on products'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'sales', 'sales_amount')
    prepopulated_fields = {'slug': ('title',)}

    action_form = UpdateActionForm
    actions = [set_discount, unset_discount]


admin.site.register(Product, ProductAdmin)


class SalesAdmin(admin.ModelAdmin):
   pass


admin.site.register(Sales, SalesAdmin)
