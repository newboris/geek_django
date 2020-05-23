from django.conf import settings
from django.db import models

from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='время', auto_now_add=True)

    @property
    def product_cost(self):
        """return cost of all products this type"""
        return self.product.price * self.quantity

    @property
    def total_quantity(self):
        """return total quantity for user"""
        items = Basket.objects.filter(user=self.user)
        totalquantity = sum([x.quantity for x in items])
        return totalquantity

    @property
    def total_cost(self):
        """return total cost for user"""
        items = Basket.objects.filter(user=self.user)
        totalcost = sum([x.product_cost for x in items])
        return totalcost

