from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse, get_resolver

from products.models import Product
from .constants import CART_ID, ITEM_TOTAL

from .models import Cart


def index(request):
    try:
        session_cart_id = request.session[CART_ID]
    except:
        session_cart_id = None
        context = {"empty": True, "message": "Your cart is empty, please keep shopping"}
    if session_cart_id:
        # carts = Cart.objects.all()
        # total = Cart.objects.aggregate(Sum("total"))
        # context = {"carts": carts, "total": total["total__sum"]}
        carts = Cart.objects.get(id=session_cart_id)

        total = 0
        for item in carts.products.all():
            total += item.price
        # total = carts.total
        # here since only one cart item can be found with the id, so we are converting the cart object to a list
        # in future if the cart is supposed to be a list, then we remove the bracket from carts variable just below to make it work
        context = {"carts": [carts], "total": total}

    template = "cart/index.html"
    return render(request, template, context)


def update_cart(request, product_slug):
    request.session.set_expiry(12000)

    try:
        session_cart_id = request.session[CART_ID]
    except:
        new_cart = Cart()
        new_cart.save()
        request.session[CART_ID] = new_cart.id
        session_cart_id = new_cart.id

    cart = Cart.objects.get(id=session_cart_id)
    # cart = Cart.objects.all()[0]
    product = Product.objects.get(slug=product_slug)

    if product not in cart.products.all():
        cart.products.add(product)
    else:
        cart.products.remove(product)
    new_total = 0
    for item in cart.products.all():
        new_total += product.price
    cart.total = new_total
    request.session[ITEM_TOTAL] = cart.products.count()
    print(f"The count of product is {cart.products.count()}")
    cart.save()

    return HttpResponseRedirect(reverse('cart_homepage'))
