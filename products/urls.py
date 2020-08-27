from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('<str:slug>/', views.single_product, name="single_product"),
    path('search', views.search, name="search_product"),
    # path('<str:slug>/<str:id>/', views.single_product),
    path('home', views.home),
    path('all', views.all_products, name='all_products'),
    path('featured', views.featured_product),
    # path('new', views.new)

]
