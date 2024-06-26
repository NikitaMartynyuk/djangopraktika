from django.core.management.base import BaseCommand
from djangoHW.hwapp3.models import Product


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        for i in range(1, 6):
            product = Product(
                title=f"product{i}",
                description=f"description{i}",
                price=i * 1.1,
                quantity=i,
            )
            product.save()
        self.stdout.write(self.style.SUCCESS("Some fake products are registered"))