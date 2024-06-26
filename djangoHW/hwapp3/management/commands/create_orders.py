import random
from django.core.management.base import BaseCommand
from djangoHW.hwapp3.models import Client, Product, Order


class Command(BaseCommand):
    help = "Create order."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = Client.objects.get(id=i)
            prods = []
            prods = [Product.objects.get(id=random.randint(1,5)) for _ in range(3)]
            order = Order.objects.create(buyer=client)
            order.products.add(*prods)
            order.calculate_total()
            order.save()

        self.stdout.write(self.style.SUCCESS("Fake orders is added"))