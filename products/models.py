from django.db import models

# from django.db.models import Model
from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.CharField(max_length=1024, blank=True, default='')
    price = models.DecimalField(decimal_places=1, max_digits=15)
    slug = models.SlugField(unique=True, auto_created=True)
    # image = models.ImageField(upload_to='products/images', null=True, default='', )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False, auto_created=True)

    def __unicode__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def get_absolute_url(self):
        # return reverse('single_product',args=[self.slug])
        return reverse('single_product',kwargs={"slug":self.slug})


class ProductImage(models.Model):
    id = models.AutoField(primary_key=True, )
    productId = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/product-images/', null=True, blank=True, default='')
    active = models.BooleanField(default=True)
