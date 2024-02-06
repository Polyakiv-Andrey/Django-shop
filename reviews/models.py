from django.db import models

from basket.models import Goods
from orders.models import Order
from products.models import Product


class Reviews(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user_id = models.CharField()

    def __str__(self):
        return self.comment
