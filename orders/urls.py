from django.urls import path

from orders.views import UserOrderListView

urlpatterns = [
    path('user/', UserOrderListView.as_view(), name="user-order-list"),
]

app_name = "orders"
