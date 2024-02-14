from django.urls import path

from payment.views import CreatePaymentAPIView, PaymentHistoryView

urlpatterns = [
    path('create-payment/', CreatePaymentAPIView.as_view(), name='create-payment'),
    path('history/', PaymentHistoryView.as_view(), name="payment-history")
]

app_name = "payment"
