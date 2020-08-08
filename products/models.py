from django.db import models

# from django.db.models import Model
from django.utils.text import slugify


class Product(models.Model):
    id = models.AutoField(primary_key=True, )
    title = models.CharField(max_length=255, null=False, blank=False)
    description = models.CharField(max_length=1024, blank=True, default='')
    price = models.DecimalField(decimal_places=1, max_digits=15)
    slug = models.SlugField(null=True, auto_created=True)
    image = models.FileField(upload_to='products/images', null=True, default='', )
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False, auto_created=True)

    def __unicode__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)
