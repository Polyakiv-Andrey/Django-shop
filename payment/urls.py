from django.urls import path

from payment.views import CreatePaymentAPIView

urlpatterns = [
    path('create-payment/', CreatePaymentAPIView.as_view(), name='create-payment'),
]

app_name = "payment"
