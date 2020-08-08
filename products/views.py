from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from products.models import Product


def index(request):
    return HttpResponse('Hi there')


def home(request):
    if request.user.is_authenticated:
        username = request.user.email
    else:
        username = request.user
    template = 'products/home.html'
    context = {"username": username}
    print(context)
    return render(request, template, context)


def all_products(request):

    template = 'products/all_product.html'
    products = Product.objects.all()

    context = {"products": products}
    return render(request, template, context)
