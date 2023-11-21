from django.shortcuts import render
from product.models import Product, ProductCategory

def home_view(request):
    categories = ProductCategory.objects.all()
    products = dict.fromkeys(categories)
    for category in categories:
        products[category] = Product.objects.filter(category=category)[:8]
    return render(request, 'homepage.html', {'products': products})

def about_view(request):
    return render(request, 'about.html')

def history_view(request):
    return render(request, 'history.html')