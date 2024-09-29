from django.shortcuts import render, get_object_or_404, redirect,reverse
from .models import Category, Product
from cart.models import Cart,CartItem
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



def category_list(request):
    categories = Category.objects.all()
    categories_with_count = []
    for category in categories:
        product_count = Product.objects.filter(category=category).count()
        categories_with_count.append({
            'category': category,
            'product_count': product_count,
        })
    return render(request, 'category.html', {'categories_with_count': categories_with_count})

def products_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category, is_visible=True)
    return render(request, 'product.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})


# views.py

def categories_view(request):
    # Получаем категории с количеством продуктов
    categories_with_count = Category.objects.annotate(product_count=Count('products'))

    return render(request, 'category.html', {
        'categories_with_count': categories_with_count,
    })


def category_home(request):
    # Получаем первые 5 категорий
    categories = Category.objects.all()[:5]
    return render(request, 'category_home.html', {'categories': categories})

@login_required
def add_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Получение или создание корзины для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Получение или создание элемента корзины для данного товара
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

    # Увеличение количества, если товар уже был в корзине
    cart_item.quantity += 1
    cart_item.save()

    # Перенаправление на страницу корзины после добавления товара
    return redirect('cart_view')

