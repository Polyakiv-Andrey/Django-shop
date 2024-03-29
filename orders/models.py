from django.db import models

from basket.models import Goods
from logistic.models import DeliveryDetail


class Order(models.Model):
    class OrderStatus:
        CREATED = "created"
        IN_PROGRESS = "in_progress"
        SHIPPED = "shipped"
        DELIVERED = "delivered"

    ORDER_STATUS_CHOICES = (
        (OrderStatus.CREATED, "Created"),
        (OrderStatus.IN_PROGRESS, "In Progress"),
        (OrderStatus.SHIPPED, "Shipped"),
        (OrderStatus.DELIVERED, "Delivered"),
    )

    delivery_status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default=OrderStatus.CREATED
    )

    delivery_info = models.ForeignKey(DeliveryDetail, on_delete=models.CASCADE, related_name="order")
    goods = models.ManyToManyField(Goods, related_name="order", blank=True)
    user_id = models.CharField()
    data_created = models.DateTimeField(auto_created=True, blank=True, null=True)

    @property
    def get_total_price(self):
        transaction = self.payment.filter(transaction_status="success").first()
        if transaction:
            return self.payment.filter(transaction_status="success").first().amount
        return None

    @property
    def get_currency(self):
        transaction = self.payment.filter(transaction_status="success").first()
        if transaction:
            return self.payment.filter(transaction_status="success").first().currency
        return None

