from django.urls import path

from logistic.views import CreateUpdateDetailDeliveryAPIView

urlpatterns = [
    path('detail/', CreateUpdateDetailDeliveryAPIView.as_view(), name="create-update-delivery-ditail"),
]

app_name = "logistic"
