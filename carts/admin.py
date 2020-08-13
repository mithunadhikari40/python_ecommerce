from django.contrib import admin

from .models import Cart


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart

    list_display = ['id', 'total', 'created', 'updated', 'active',
                    'deleted']

    search_fields = ['total', ]
    list_editable = ['total', 'active', 'deleted']
    list_filter = ['active', 'total', 'deleted']
    date_hierarchy = 'created'
    readonly_fields = ['created', 'updated']


admin.site.register(Cart, CartAdmin)
