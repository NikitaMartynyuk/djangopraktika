# Generated by Django 5.0.6 on 2024-06-19 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinFlip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.CharField(choices=[('H', 'Heads'), ('T', 'Tails')], max_length=1)),
                ('flip_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
