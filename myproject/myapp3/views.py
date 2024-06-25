import logging
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from datetime import timedelta
from .models import Order, Client

logger = logging.getLogger(__name__)


def index(request):
    context = {
        "title": "Главная страница",
    }
    logger.info("Index page accessed")
    return render(request, "myapp3/index.html", context)


def orders(request, client_id: int = None):
    if client_id:
        client = get_object_or_404(Client, id=client_id)
        order = Order.objects.filter(buyer=client)
        today = timezone.now()

        # Заказы клиента за период времени
        order_week = order.filter(order_date__gte=today - timedelta(days=7))
        order_month = order.filter(order_date__gte=today - timedelta(days=30))
        order_year = order.filter(order_date__gte=today - timedelta(days=365))

        # Получаем уникальные продукты в заказах
        products_week = {product for order in order_week for product in order.products.all()}
        products_month = {product for order in order_month for product in order.products.all()}
        products_year = {product for order in order_year for product in order.products.all()}

        context = {
            "title": f"Список заказов клиента {client.name}",
            "client": client,
            "order": order,
            "products_week": products_week,
            "products_month": products_month,
            "products_year": products_year,
        }
    else:
        order = Order.objects.all()
        context = {"title": f"Список всех заказов", "order": order}
    return render(request, "myapp3/orders.html", context)