from django.db import models
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem

# Create your models here.
# here we are decoupling the tags app from the store app
# since we want tags on our products we are using a GenericForeignKey
class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem

# we are extending the ProductAdmin class from the store app
class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

# we are unregistering the Product model from the admin site
admin.site.unregister(Product)
# we are registering the Product model with the CustomProductAdmin class
admin.site.register(Product, CustomProductAdmin)