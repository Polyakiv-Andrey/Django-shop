from django.db import models
from django.utils import timezone

from basket.models import Goods
from logistic.models import DeliveryDetail
from orders.models import Order
from products.models import Product


class Reviews(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="reviews")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    user_id = models.CharField()
    date_created = models.DateTimeField(auto_now=True, blank=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        if self.comment:
            return self.comment
        return "Good product!!!"

    def save(self, *args, **kwargs):
        self.date = timezone.now()
        super().save(*args, **kwargs)

    @property
    def get_reviewer(self):
        delivery = DeliveryDetail.objects.get(user_id=self.user_id)
        return delivery.first_name.capitalize() + " " + delivery.last_name.capitalize()

    @property
    def get_date(self):
        if self.date_updated:
            return self.date_updated
        return self.date_created
