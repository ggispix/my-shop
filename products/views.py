from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from django.shortcuts import render
from .models import Category, Product

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
    products = Product.objects.all()
    return render(request, 'product.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
