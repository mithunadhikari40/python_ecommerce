from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render

from .models import Cart


def index(request):
    carts = Cart.objects.all()
    total = Cart.objects.aggregate(Sum("total"))
    context = {"carts": carts, "total": total["total__sum"]}

    template = "cart/index.html"
    return render(request, template, context)
