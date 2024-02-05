from django.urls import path

from logistic.views import CreateUpdateDetailDeliveryView

urlpatterns = [
    path('detail/', CreateUpdateDetailDeliveryView.as_view(), name="create-update-delivery-ditail"),
]

app_name = "logistic"
