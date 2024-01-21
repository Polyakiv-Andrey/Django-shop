from django.db import models

from products.models import Product


class Goods(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="goods")
    amount = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name} - {self.amount}"


class Basket(models.Model):
    goods = models.ManyToManyField('Goods', related_name="basket")
    user_id = models.CharField(unique=True)

    def __str__(self):
        return self.user_id