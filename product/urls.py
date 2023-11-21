from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_view, name='product_list'),
    path('<int:product_id>/', views.product_detail_view, name='product_detail'),
]
