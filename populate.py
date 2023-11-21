import os, json, sys
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazar_digital.settings')
django.setup()

from product.models import Product, ProductCategory 

faker = Faker()

def create_categories(n):
    categories = []
    for _ in range(n):
        name = faker.word().capitalize()
        description = faker.text()
        is_active = faker.boolean()
        category = ProductCategory(name=name, description=description, is_active=is_active)
        categories.append(category)
    ProductCategory.objects.bulk_create(categories)
    return categories

def create_products(n, categories):
    for _ in range(n):
        product = Product(
            name=faker.catch_phrase(),
            description=faker.text(),
            price=faker.pydecimal(left_digits=4, right_digits=2, positive=True),
            stock=faker.random_int(min=0, max=100),
            is_active=faker.boolean(),
            category=random.choice(categories),
        )
        product.save()

def remove_products():
    with open('products_ids.json', 'r') as f:
        products_ids = json.load(f)
    for product_id in products_ids:
        product = Product.objects.get(id=product_id)
        product.delete()

def remove_categories():
    with open('categories_ids.json', 'r') as f:
        categories_ids = json.load(f)
    for category_id in categories_ids:
        category = ProductCategory.objects.get(id=category_id)
        category.delete()

if "delete" in sys.argv:
    remove_products()
    remove_categories()
    print("Dados fictícios removidos com sucesso")
elif "populate" in sys.argv:
    num_categories = 10
    num_products = 100

    categories = create_categories(num_categories)
    create_products(num_products, categories)

    products_ids = []
    for product in Product.objects.all():
        products_ids.append(product.id)

    with open('products_ids.json', 'w') as f:
        json.dump(products_ids, f)

    with open("categories_ids.json", "w") as f:
        json.dump([category.id for category in categories], f)
    print("Dados fictícios inseridos com sucesso!")
else:
    print("Comando inválido.\nUtilize\n'python populate.py populate'\npara inserir dados fictícios ou \n'python populate.py delete'\npara removê-los")
