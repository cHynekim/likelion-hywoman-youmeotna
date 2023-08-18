from django.shortcuts import render, redirect

from .cart import Cart
from shop.models import Product


def detail(request):
    cart = Cart(request)
    cart_items = list(cart)
    total_price = cart.get_product_total()

    return render(request, 'cart/detail.html', {'cart':cart_items, 'total_price':total_price})

def product_add(request, product_id):
    if request.method == "POST":
        cart = Cart(request)
        product = Product.objects.get(id=product_id)
        cart.add(product=product, quantity=1, is_update=True)
        return redirect('cart:cart')
    else:
        return redirect('cart:cart')

def remove(request, product_id):
    cart = Cart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect('cart:cart')

def clear(request):
    cart = Cart(request)
    cart.clear(request)
    return redirect('cart:cart')

def order_start(request):
    cart = Cart(request)
    cart_items = list(cart)
    total_price = cart.get_product_total()
    return render(request, 'order/payment.html', {'cart':cart_items, 'total_price':total_price})