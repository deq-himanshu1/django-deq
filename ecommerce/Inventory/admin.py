from django.contrib import admin
from Inventory.models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)