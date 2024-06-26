from django.db import models


class CoinFlip(models.Model):
    HEADS = 'H'
    TAILS = 'T'
    FLIP_CHOICES = [
        ('H', 'Heads'),
        ('T', 'Tails'),
    ]

    result = models.CharField(choices=FLIP_CHOICES, max_length=1)
    flip_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.result} flipped at {self.flip_time}'