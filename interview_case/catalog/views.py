from gc import get_objects
from multiprocessing import context
from unicodedata import category
from urllib import request
from django.shortcuts import render, get_object_or_404
from .models import Categories, Product
from cart.forms import CartAddProductForm
# Create your views here.


def main_view(request):
    category = Categories.objects.all()
    return render(request, 'catalog/base.html' , {'category': category})
  
def catalog_view(request, id = None , category_slug = None):
    if id:
        product = get_object_or_404(Product, id=id)  
        cart_product_form = CartAddProductForm()
        page = 'catalog/product.html'
        context = {'product': product,
                   'cart_product_form': cart_product_form
                   }
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        products = Product.objects.filter(category = category)
        page = 'catalog/category.html'
        context = {'category': category,
                   'products': products
                   }
        
    return render(request, page, context)