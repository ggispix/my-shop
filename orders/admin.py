from django.contrib import admin
from .models import Order, OrderItem, OrderInfo

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Убираем пустые строки для создания новых элементов

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_price')
    list_filter = ('created_at', 'user')  # Фильтры по дате создания и пользователю
    inlines = [OrderItemInline]  # Отображение связанных товаров прямо в заказе

class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'city', 'address', 'final_price')
    search_fields = ('full_name', 'email', 'city')  # Добавляем поиск

# Регистрируем модели в админке
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderInfo, OrderInfoAdmin)
