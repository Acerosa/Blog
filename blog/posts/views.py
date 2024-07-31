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







