from django.db import models
from django.shortcuts import render
from django.utils import timezone


class OrderItem:
    pass


# Create your models here.
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Задача'
        verbose_name_plural = 'Задачи'


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    numbers = models.IntegerField()
    address = models.TextField()
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField( )
    quantity = models.IntegerField()
    dateTime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)


    def calculate_total_amount(self):
        total = sum(product.price *
                    product.quantity for product in self.products.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.user.name}"


def customer_order_history(request):
    customer = request.user

    orders_last_week = customer.orders.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=7)
    )
    orders_last_month = customer.orders.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=30)
    )
    orders_last_year = customer.orders.filter(
        created_at__gte=timezone.now() - timezone.timedelta(days=365)
    )

    # Получаем уникальные товары из заказов
    unique_products_last_week = set()
    for order in orders_last_week:
        for item in order.orderitems.all():
            unique_products_last_week.add(item.product)

    unique_products_last_month = set()
    for order in orders_last_month:
        for item in order.orderitems.all():
            unique_products_last_month.add(item.product)

    unique_products_last_year = set()
    for order in orders_last_year:
        for item in order.orderitems.all():
            unique_products_last_year.add(item.product)

    # Сортировка товаров по времени последнего заказа
    sorted_products_last_week = sorted(
        unique_products_last_week,
        key=lambda product: product.orders.filter(
            created_at__gte=timezone.now() - timezone.timedelta(days=7)
        ).order_by('-created_at').first().created_at,
        reverse=True,
    )

    sorted_products_last_month = sorted(
        unique_products_last_month,
        key=lambda product: product.orders.filter(
            created_at__gte=timezone.now() - timezone.timedelta(days=30)
        ).order_by('-created_at').first().created_at,
        reverse=True,
    )

    sorted_products_last_year = sorted(
        unique_products_last_year,
        key=lambda product: product.orders.filter(
            created_at__gte=timezone.now() - timezone.timedelta(days=365)
        ).order_by('-created_at').first().created_at,
        reverse=True,
    )

    context = {
        'sorted_products_last_week': sorted_products_last_week,
        'sorted_products_last_month': sorted_products_last_month,
        'sorted_products_last_year': sorted_products_last_year,
    }
    return render(request, 'customer_order_history.html', context)