from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}): {message}')
    return render(request, 'catalog/contacts.html')

def catalog(request):
    product_list = Product.objects.all()
    content = {
        'object_list': product_list
    }
    return render(request, 'catalog/catalog.html', content)
