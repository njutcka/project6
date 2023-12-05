from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    product_list = Product.objects.all()
    content = {
        'object_list': product_list,
        'title': 'Skystore',
    }
    return render(request, 'catalog/home.html', content)

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


def product(request: HttpRequest, product_id: int):
    """представление страницы main/product.html для каждого продукта"""
    product = get_object_or_404(Product, pk=product_id)
    content = {
        'product': product,
        'title': 'Продукт',
    }
    return render(request, 'catalog/product.html', content)
