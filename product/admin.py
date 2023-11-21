from django.contrib import admin
from .models import Product, ProductCategory

# Registro do modelo Product para o Django Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_active', 'created_at', 'updated_at', 'category']
    list_filter = ['is_active', 'category']
    search_fields = ['name', 'description', 'category__name']

# Registro do modelo ProductCategory para o Django Admin
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
