from django.views import generic

from orders.models import Order


class UserOrderListView(generic.ListView):
    model = Order
    template_name = 'shop/order-list.html'

    def get_queryset(self):
        user_id = self.request.COOKIES.get("user_id")
        return Order.objects.filter(user_id=user_id)
