from django.shortcuts import render
from django.views.generic import ListView
from Inventory.models import Product
from Inventory.models import Category

# Create your views here.
class ProductListView(ListView):
    model = Product
    template_name = 'Inventory/product.html'
    context_object_name = 'products_list'

class CategoryListView(ListView):
    model = Category
    template_name = 'Inventory/category.html'
