import random

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category_list = [
            {'category': 'категория 1', 'description_category': 'описание категории 1'},
            {'category': 'категория 2', 'description_category': 'описание категории 2'},
            {'category': 'категория 3', 'description_category': 'описание категории 3'},
            {'category': 'категория 4', 'description_category': 'описание категории 4'},
            {'category': 'категория 5', 'description_category': 'описание категории 5'}
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)

        product_list = [
            {'name': 'Товар 1', 'description_product': 'описание товара 1', 'image': '', 'category': 'категория 1', 'price': '12', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 2', 'description_product': 'описание товара 2', 'image': '', 'category': 'категория 4', 'price': '12', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 3', 'description_product': 'описание товара 3', 'image': '', 'category': 'категория 3', 'price': '11', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 4', 'description_product': 'описание товара 4', 'image': '', 'category': 'категория 1', 'price': '13', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 5', 'description_product': 'описание товара 5', 'image': '', 'category': 'категория 3', 'price': '21', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 6', 'description_product': 'описание товара 6', 'image': '', 'category': 'категория 2', 'price': '22', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 7', 'description_product': 'описание товара 7', 'image': '', 'category': 'категория 5', 'price': '33', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 8', 'description_product': 'описание товара 8', 'image': '', 'category': 'категория 2', 'price': '4', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 9', 'description_product': 'описание товара 9', 'image': '', 'category': 'категория 1', 'price': '54', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
            {'name': 'Товар 10', 'description_product': 'описание товара 10', 'image': '', 'category': 'категория 4', 'price': '32', 'date_of_creation': '2000-01-01', 'last_modified_date': '2000-01-01'},
        ]

        for product_item in product_list:
            Product.objects.create(**product_item)

        Product.objects.bulk_create(product_list)