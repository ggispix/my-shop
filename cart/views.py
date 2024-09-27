from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import AnonymousUser
from django.db.models import Sum
from .models import Product, Cart, CartItem
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        # Обновление общей стоимости корзины
        total_price = cart.cartitem_set.aggregate(total=Sum('product__price'))['total']

        return redirect('cart')


def cart_view(request):
    if isinstance(request.user, AnonymousUser):
        return redirect('login')
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = cart_items.aggregate(total=Sum('product__price'))['total']
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
