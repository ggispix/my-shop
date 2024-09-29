from django.urls import path
from .views import category_list,product_detail,products_by_category, add_product
from cart.views import cart_view

app_name = 'products'

urlpatterns = [
    path('products/', category_list, name='category_list'),
    path('products/<int:category_id>/', products_by_category, name='product_list'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('add-to-cart/<int:product_id>/', add_product, name='add_to_cart'),
    path('cart/', cart_view, name='cart_view'),
    # Новый маршрут для деталей продукта
]

