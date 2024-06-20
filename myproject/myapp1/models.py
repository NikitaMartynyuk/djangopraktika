from django.db import models


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

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.user = None
        self.id = None
        self.products = None

    def calculate_total_amount(self):
        total = sum(product.price *
                    product.quantity for product in self.products.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.user.name}"