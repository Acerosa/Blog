# Update urls.py to use CBVs
from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductDeleteView,
)

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
]