from django.urls import path
from . import views


urlpatterns = [
    path('customer/', views.customer_order_history, name='customer_order_history'),
]