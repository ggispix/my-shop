from django.shortcuts import render, get_object_or_404,redirect
from cart.models import Cart
from .form import  OrderForm

def checkout(request):
    cart = Cart.objects.get(user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = sum(item.product.price * item.quantity for item in cart.cartitem_set.all())
            order.save()
            return redirect('order_success')
    else:
        form = OrderForm()
    return render(request, 'checkout.html', {'form': form})

