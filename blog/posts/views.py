from .models import Product
from .forms import ProductForm
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/pDetails.html'
    context_object_name = 'product'

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'myapp/edit.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'myapp/delete.html'
    success_url = reverse_lazy('product_list')

