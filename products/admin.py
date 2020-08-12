from django.contrib import admin
from .models import Product,ProductImage


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',

        "title",
        "description",
        "price",
        "slug",
        # 'get_image',
        "created",
        "updated",
        "active",
        'deleted'
    )
    search_fields = ['title', 'price', 'slug']
    list_editable = ['price', 'active', 'description']
    list_filter = ['active', 'price', 'deleted']
    date_hierarchy = 'created'
    readonly_fields = ['created', 'updated']
    prepopulated_fields = {"slug": ["title"]}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
