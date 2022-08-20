
from unicodedata import category
from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Product, Categories, Sales
from .admin_services import UpdateActionForm, set_discount, unset_discount
from django.utils.html import format_html


class CategoriesAdmin(DjangoMpttAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title_display', 'products')
    list_display_links = ('title_display',)
    mptt_level_indent = 20

    def title_display(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.title,  # Or whatever you want to put here
        )
    title_display.short_description = ('title')
    
    @admin.display(empty_value='products')
    def products(self, obj):
        return Product.objects.filter(category_id=obj.id).count()
    
        
        


admin.site.register(Categories, CategoriesAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category',
                    'sales', 'sales_amount', )
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('sales',)
    search_fields= ('title',)
    
    action_form = UpdateActionForm
    actions = [set_discount, unset_discount]


admin.site.register(Product, ProductAdmin)


class SalesAdmin(admin.ModelAdmin):
   pass


admin.site.register(Sales, SalesAdmin)
