from django.db import models

# Create your models here.
from django.db.models import Sum

from products.models import Product


class Cart(models.Model):
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False, auto_created=True)

    def __unicode__(self):
        return f"Cart id {self.id}"

    def total_amount(self):
        amount = Cart.objects.annotate(total_amount=Sum('total'))
        return amount.total_amount
