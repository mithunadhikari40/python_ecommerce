from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, get_resolver

from products.models import Product

from .models import Cart


def index(request):
    carts = Cart.objects.all()
    total = Cart.objects.aggregate(Sum("total"))
    context = {"carts": carts, "total": total["total__sum"]}

    template = "cart/index.html"
    return render(request, template, context)


def update_cart(request, product_slug):
    cart = Cart.objects.all()[0]
    product = None
    try:
        product = Product.objects.get(slug=product_slug)

    except:
        pass
    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    new_total = 0
    for item in cart.products.all():
        new_total += product.price
    cart.total = new_total
    cart.save()

    return HttpResponseRedirect(reverse("cart"))
