from django.core.management.base import BaseCommand
from djangoHW.hwapp3.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        global client
        for i in range(1, 5):
            client = Client(
                name=f"Client {i}",
                email=f"example{i}@mail.com",
                phone=f"+7({i}{i}{i})-222-33-33",
                address="Ekb",
            )
            client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))