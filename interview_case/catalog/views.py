from django.shortcuts import render, get_object_or_404
from .models import Product
from cart.forms import CartAddProductForm

# Create your views here.


def main_view(request):
    product = Product.objects.all()
    return render(request, 'catalog/base.html' , {"product": product})


def catalog_view(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'catalog/catalog.html', {'product': product,
                                                 'cart_product_form': cart_product_form,
                                                 })