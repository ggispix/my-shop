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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import about_us,orders,cart,products,contacts
from django.urls import path

import register.views
import subscription.views
from about_us.views import aboutUs
from cart.views import cart_view
from my_shop_project import settings
from orders.views import checkout,order_success
from products.views import product_detail, products_by_category, category_list,add_product
from contacts.views import index
from subscription import views
from register import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', aboutUs, name='about_us'),  # Home page

    path('about-us/', include(('about_us.urls', 'about_us_app'), namespace='about_us')),

    path('cart/', include(('cart.urls', 'cart_app'), namespace='cart')),# Cart page
    path('cart/', cart_view, name='cart_view'),
    path('order/', include('orders.urls')),
    path('order-success/', order_success, name='order_success'),


    path('order/', include(('orders.urls', 'orders_app'), namespace='orders')),# Orders page

    path('categories/', include(('products.urls', 'products_app'), namespace='products')),

    path('subscription/', include(('subscription.urls', 'subscription_app'), namespace='subscription')),

    path('product/', include(('products.urls', 'product_app'), namespace='product')),

    path('category/<int:category_id>/', products_by_category, name='products_by_category'),

    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('product/<int:product_id>/<int:cart_id>', add_product, name='add_product'),

    path('subscription/', subscription.views.subscribe, name='subscription'),

    path('register/', register.views.register, name='register'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Страница логина
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('checkout/', include(('orders.urls', 'order_app'), namespace='checkout')),

    path('login/', views.user_login, name='login'),

    path('logout/', views.user_logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
