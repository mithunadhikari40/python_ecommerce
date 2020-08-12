import os

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
from ecommerce.settings import BASE_DIR
from products.models import Product, ProductImage


def index(request):
    template = 'products/index.html'
    products = Product.objects.all()

    context = {"products": products}
    return render(request, template, context)


def home(request):
    if request.user.is_authenticated:
        username = request.user.email
    else:
        username = request.user
    template = 'products/home.html'
    context = {"username": username}
    print(os.path.join(BASE_DIR, "static", "static_root"))
    return render(request, template, context)


def all_products(request):
    template = 'products/all_product.html'
    products = Product.objects.all()

    context = {"products": products}
    return render(request, template, context)


def featured_product(request):
    template = 'products/featured_products.html'
    products = Product.objects.all()
    path = os.path.abspath(os.path.dirname(__file__))
    print(f"The full path is now {path}")
    path = os.path.realpath(path)
    print(f"The relative path is now {path}")

    context = {"products": products, "path": path}
    return render(request, template, context)


def single_product(request, slug):
    product = Product.objects.get(slug=slug)

    # this will find all the images object associated with this product with foreign key relationship
    images = ProductImage.objects.filter(productId=product)

    template = 'products/single_product.html'

    context = {"product": product, "images": images}
    return render(request, template, context)


def search(request):
    try:
        name = request.GET.get('name')

    except:
        name = None
    template = 'products/search_results.html'

    if name:
        template = 'products/search_results.html'
        products = Product.objects.filter(title__icontains=name)

        context = {"query": name, "products": products}
    else:
        context = {}

    print(f"The searched name is now {name}")
    return render(request, template, context)
