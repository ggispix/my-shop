from django.db import models
from django.utils import timezone


class Category(models.Model):
    photo =models.ImageField(upload_to="category")
    name = models.CharField(max_length=50)
    sort = models.PositiveSmallIntegerField()
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['sort']

class Sale(models.Model):
    name = models.CharField(max_length=50)  # the name of sale
    discount = models.DecimalField(max_digits=5, decimal_places=2)  # percent of sale
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.discount}; {self.start_date} - {self.end_date}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='product_photos')
    description = models.TextField()
    is_visible = models.BooleanField(default=True)
    sales = models.ManyToManyField(Sale, blank=True)  # list of discounts for product

    def final_price(self):
        active_sales = self.sales.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if active_sales.exists():
            max_discount = max(sale.discount for sale in active_sales)
            final_price = self.price * (1 - max_discount / 100)
            return final_price
        return self.price

    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'


    def __str__(self):
        return self.name
