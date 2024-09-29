from .views import register, user_login,user_logout
from django.urls import path
from django.contrib.auth import views as auth_views



name = 'register'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/',user_logout, name='logout'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]