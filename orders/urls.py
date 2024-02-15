from django.urls import path

from orders.views import UserOrderListView, AdminOrderListView, ChangeOrderStatusView

urlpatterns = [
    path('user/', UserOrderListView.as_view(), name="user-order-list"),
    path('admin/', AdminOrderListView.as_view(), name="admin-order-list"),
    path('change-status/<int:id>/', ChangeOrderStatusView.as_view(), name="change-order-status")
]

app_name = "orders"
