from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class Product(models.Model):
    name = models.CharField(verbose_name=_("Name"),default=None, blank=True, null=True,max_length=20)
    title = models.CharField(verbose_name=_("Title"),default=None, blank=True, null=True,max_length=20)
    content = models.CharField(verbose_name=_("Content"),default=None, blank=True, null=True,max_length=100)
    pro_date = models.DateTimeField(verbose_name=_("Production Date"),default=None, blank=True, null=True)
    number = models.IntegerField(verbose_name=_("Number"),default=None, blank=True, null=True)
    price = models.FloatField(verbose_name=_("Price"),default=None, blank=True, null=True)


class Order(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    date = models.DateTimeField(verbose_name=_("Order Date"),default=None, blank=True, null=True)
    status = models.CharField(verbose_name=_("Order Status"),default=None, blank=True, null=True,max_length=20)

class Item(models.Model):
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
    )
