from django.shortcuts import render, redirect
from .models import Product, ProductCategory

def product_detail_view(request, product_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        stock = request.POST.get('stock')
        category_id = request.POST.get('category_id')
        category = ProductCategory.objects.get(id=category_id)

        product = Product(name=name, description=description, price=price, stock=stock, category=category)
        product.save()
    elif request.method == 'DELETE':
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)
        product.delete()
    elif request.method == 'UPDATE':
        product_id = request.GET.get('product_id')
        product = Product.objects.get(id=product_id)
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.price = request.POST.get('price')
        product.stock = request.POST.get('stock')
        product.category_id = request.POST.get('category_id')
        product.save()
    elif request.method == 'GET':
        product = Product.objects.get(id=product_id)

        return render(request, 'product/product_detail.html', {'product': product})

    return redirect('product_list')

def product_list_view(request):
    category = request.GET.get('category', None)
    products = Product.objects.all()
    if category:
        products = products.filter(category__name=category)
    return render(request, 'product/product_list.html', {'products': products, 'category': category})

def category_detail_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        category = ProductCategory(name=name, description=description)
        category.save()

    return redirect('product_list')

def category_list_view(request):
    order_by = request.GET.get('order_by', 'name')
    categories = ProductCategory.objects.all().order_by(order_by)

    return render(request, 'product/category_list.html', {'categories': categories})