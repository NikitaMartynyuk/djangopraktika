from django.core.management.base import BaseCommand
from myproject.myapp3.models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        for i in range(1, 5):
            client = Client (
                name=f"Client {i}",
                email=f"example{i}@mail.com",
                phone=f"+7({i}{i}{i})-111-22-33",
                address="Spb",
            )
            client.save()
        self.stdout.write(self.style.SUCCESS(f"Client:'{client}' is registered"))
