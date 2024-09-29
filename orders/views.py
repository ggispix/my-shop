from django.shortcuts import render, get_object_or_404, redirect
from cart.models import Cart, CartItem
from orders.models import Order, OrderItem, OrderInfo
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.contrib import messages

@login_required
@transaction.atomic
def checkout(request):
    # Получаем корзину пользователя
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if not cart_items.exists():
        messages.info(request, "Your cart is empty.")
        return redirect('cart_view')

    # Подсчитываем общую стоимость
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    # Проверяем наличие товара на складе (необязательно)
    for item in cart_items:
        if item.product.stock < item.quantity:
            messages.error(request, f"Not enough stock for {item.product.name}")
            return redirect('cart_view')

    # Создаем заказ и связываем его с корзиной
    order = Order.objects.create(user=request.user, total_price=total_price, cart=cart)

    # Переносим товары из корзины в заказ
    for item in cart_items:
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    # Очищаем корзину
    cart_items.delete()

    # Перенаправляем на страницу успешного заказа
    return reverse('app_name:order_success', kwargs={'pk': order.pk})

def order_success(request):
    return render(request, 'checkout_2.html',)

def order_checkout(request):
    return render(request, 'checkout.html')




def order_summary(request, order_id):
    # Получаем заказ по ID, если он принадлежит пользователю
    order = get_object_or_404(Order, id=order_id, user=request.user)

    # Получаем элементы заказа
    order_items = order.items.all()

    # Получаем информацию о пользователе
    order_info = OrderInfo.objects.filter(user=request.user).last()  # Последняя информация о заказе

    context = {
        'order': order,
        'order_items': order_items,
        'order_info': order_info,
    }

    return render(request, 'checkout_2.html', context)

def payment_view(request):
    # Логика обработки платежа
    return render(request, 'payment.html')

def payment_succeed(request):
    # Логика обработки платежа
    return render(request, 'checkout_3.html')

