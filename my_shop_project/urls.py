"""
URL configuration for my_shop_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import about_us,orders,cart,products,contacts
from django.urls import path
from about_us.views import aboutUs
from cart.views import cart_view
from orders.views import checkout
from products.views import product_detail, products_by_category, category_list
from contacts.views import index


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', aboutUs, name='about_us'),  # Home page

    path('about-us/', include(('about_us.urls', 'about_us_app'), namespace='about_us')),

    path('cart/', include(('cart.urls', 'cart_app'), namespace='cart')),# Cart page

    path('orders/', include(('orders.urls', 'orders_app'), namespace='orders')),# Orders page

    path('categories/', include(('products.urls', 'products_app'), namespace='products')),
    path('category/<int:category_id>/', products_by_category, name='products_by_category'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]

