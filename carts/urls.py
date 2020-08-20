from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='cart'),
    path('<str:product_slug>/', views.update_cart, name="update_cart"),
    # path('search', views.search, name="search_product"),
    # # path('<str:slug>/<str:id>/', views.single_product),
    # path('home', views.home),
    # path('all', views.all_products),
    # path('featured', views.featured_product),
    # path('new', views.new)

]
