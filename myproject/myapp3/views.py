from django.http import HttpResponse
from django.shortcuts import render



def customer_order_history(request, sorted_products_last_year=None, sorted_products_last_month=None,
                                sorted_products_last_week=None):
        context = {
            'sorted_products_last_week': sorted_products_last_week,
            'sorted_products_last_month': sorted_products_last_month,
            'sorted_products_last_year': sorted_products_last_year,
        }
        return HttpResponse( 'context', context)

