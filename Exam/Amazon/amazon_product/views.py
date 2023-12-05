from typing import Any

from django.contrib import messages
from django.db import models
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import Product_Forms
from .models import Product



class AddProductView(CreateView):
    modal = Product
    form_class = Product_Forms
    template_name = 'add_your_product.html'
    success_url = '/product/'

    def post(self, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            book = form.save(commit=False)
            book.author = self.request.user
            book.save()
        return redirect('product_view')




class ProductListView(ListView):
    modal = Product
    template_name = 'products.html'

    def get_queryset(self):
        return Product.objects.all()


class ProductDetailsView(DetailView):
    modal = Product
    template_name = 'product_details.html'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])


class ProductUpdateView(UpdateView):
    modal = Product
    form_class = Product_Forms
    template_name = 'update_product.html'
    success_url = '/product/'

    def get_queryset(self):
        return Product.objects.filter(id=self.kwargs['pk'])




def delete_book(request, book_id: int):
    book = Product.objects.get(id=book_id)
    book.delete()
    messages.success(request, 'Product deleted successfully!')
    return redirect('product_view')