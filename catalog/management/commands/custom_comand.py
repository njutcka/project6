from django.core.management import BaseCommand
from catalog.models import Category, Product
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        return os.system("python3 manage.py loaddata data_catalog.json")

