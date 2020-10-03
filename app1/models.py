from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField()
    title = models.CharField()
    content = models.CharField()
    pro_date = models.DateTimeField()
    number = models.IntegerField()
    price = models.FloatField()


class Order(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date = models.DateTimeField()
    status = models.CharField()

class Item(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    order = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
