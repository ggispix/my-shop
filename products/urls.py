from django.urls import path
from .views import category_list,product_detail,products_by_category

app_name = 'products'

urlpatterns = [
    path('products/', category_list, name='category_list'),
    path('products/<int:category_id>/', products_by_category, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),  # Новый маршрут для деталей продукта
]

