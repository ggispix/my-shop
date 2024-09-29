from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required


@login_required
def add_to_cart(request, product_id):
    # Получаем продукт
    product = get_object_or_404(Product, id=product_id)

    # Получаем или создаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Получаем или создаем элемент корзины для этого продукта
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Увеличиваем количество товара в корзине
    cart_item.quantity += 1
    cart_item.save()

    # Перенаправляем пользователя на страницу корзины
    return redirect('cart_view')


@login_required
def cart_view(request):
    # Получаем корзину пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Получаем все элементы корзины
    cart_items = CartItem.objects.filter(cart=cart)

    # Создаем список с данными товаров в корзине
    cart_items_data = []
    for item in cart_items:
        cart_items_data.append({
            'name': item.product.name,
            'price': item.product.price,
            'quantity': item.quantity,
            'image_url': item.product.photo.url,  # Предполагаем, что у Product есть поле photo
            'url': '#',  # Здесь можно добавить URL продукта, если нужно
        })

    # Подсчитываем стоимость корзины
    cart_subtotal = sum(item['price'] * item['quantity'] for item in cart_items_data)
    shipping_fee = 99  # Пример фиксированной стоимости доставки
    tax = 231  # Пример налога
    cart_total = cart_subtotal + shipping_fee + tax
    total_items = sum(item['quantity'] for item in cart_items_data)

    # Передаем данные в шаблон
    context = {
        'cart_items': cart_items_data,
        'cart_subtotal': cart_subtotal,
        'shipping_fee': shipping_fee,
        'tax': tax,
        'cart_total': cart_total,
        'total_items': total_items,
    }
    return render(request, 'cart.html', context)
