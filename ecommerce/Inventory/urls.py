from django.urls import path
from Inventory import views
from Inventory.views import ProductListView
urlpatterns = [
    path('product/',ProductListView.as_view(),name='products'),
    path('category/',ProductListView.as_view(),name='category')
]