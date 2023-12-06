from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    content = {
        'title': 'Контакты',
    }
    return render(request, 'catalog/contacts.html', content)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'
