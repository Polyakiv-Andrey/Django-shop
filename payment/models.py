from django.db import models

from logistic.models import DeliveryDetail
from orders.models import Order


class Payments(models.Model):
    class TransactionStatus:
        success = "success"
        pending = "pending"
        failed = "failed"

    TRANSACTION_STATUS = (
        (TransactionStatus.success, "Success"),
        (TransactionStatus.pending, "Pending"),
        (TransactionStatus.failed, "Failed"),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField()
    delivery_ditail = models.ForeignKey(DeliveryDetail, on_delete=models.CASCADE, related_name="payment")
    data_created = models.DateTimeField(auto_created=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payment")
    transaction_status = models.CharField(choices=TRANSACTION_STATUS, default=TransactionStatus.pending)

    def __str__(self):
        return self.amount


