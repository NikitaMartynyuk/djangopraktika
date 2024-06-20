from django.http import HttpResponse
from django.shortcuts import render
from .models import CoinFlip


# Create your views here.
# def coin_flip_view(request):
#     flips = CoinFlip.objects.all()
#     return render(request, 'coin_flip_template.html', {'flips': flips})


def coin(request):
    flips = CoinFlip.objects.all()
    return HttpResponse(f'flips: {flips}')


