from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Product, Categories

class CategoriesAdmin(DjangoMpttAdmin):
    prepopulated_fields =  {'slug' : ('title',)}
    
admin.site.register(Categories, CategoriesAdmin)

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('title',)}
    
admin.site.register(Product, ProductAdmin)