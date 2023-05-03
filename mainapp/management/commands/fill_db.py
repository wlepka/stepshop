import json
import os

# from django.contrib.auth.models import User
from django.core import management
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = os.path.join('mainapp', 'fixtures')


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name), mode='r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories.json')
        # ProductCategory.objects.all().delete()

        products = load_from_json('products.json')
        # Product.objects.all().delete()

        for category in categories:
            _category = category.get('fields')
            _category['id'] = category.get('pk')

            new_category = ProductCategory(**_category)
            new_category.save()

        for product in products:
            _product = product.get('fields')
            category_id = _product.get('category')
            _product['category'] = ProductCategory.objects.get(pk=category_id)

            new_product = Product(**_product)
            new_product.save()

        # User.objects.create_superuser('admin', 'admin@stepshop.local', '123')
        ShopUser.objects.create_superuser('admin', 'admin@stepshop.local', '123', age=30)
