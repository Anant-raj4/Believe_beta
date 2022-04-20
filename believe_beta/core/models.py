from django.db import models

# Create your models here.


class Consumer(models.Model):
    consumer_name = models.CharField(max_length=100)
    consumer_email = models.EmailField(max_length=200)

    PUJA_TYPES = (
        ('GP', 'Ganesh Puja'),
        ('LP', 'Lakshmi Puja'),
        ('SP', 'Satyanarayan Puja')
    )

    consumer_puja = models.CharField(max_length=100, choices=PUJA_TYPES)

    PANDIT_NAME = (
        ('A', "Abhi"),
        ('B', "Shado"),
        ('C', "Lado"),
        ('d', "Hado")
    )
    consumer_pandit = models.CharField(max_length=2, choices=PANDIT_NAME)
    consumer_age = models.IntegerField(default=18)
    puja_date = models.DateField()
    puja_time = models.TimeField()
