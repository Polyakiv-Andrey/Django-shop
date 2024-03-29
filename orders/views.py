from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.views import generic

from orders.models import Order


class UserOrderListView(generic.ListView):
    model = Order
    template_name = 'shop/order-list.html'
    context_object_name = 'order_list'
    paginate_by = 5

    def get_queryset(self):
        user_id = self.request.COOKIES.get("user_id")
        return Order.objects.filter(user_id=user_id).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(UserOrderListView, self).get_context_data(**kwargs)
        list_orders = self.get_queryset()
        paginator = Paginator(list_orders, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            orders = paginator.page(page)
        except PageNotAnInteger:
            orders = paginator.page(1)
        except EmptyPage:
            orders = paginator.page(paginator.num_pages)

        context['order_list'] = orders
        return context


class AdminOrderListView(generic.ListView):
    model = Order
    template_name = 'adminPanel/order-list.html'
    context_object_name = 'order_list'
    paginate_by = 5
    queryset = Order.objects.all().order_by('data_created')


class ChangeOrderStatusView(generic.View):

    def post(self, request, *args, **kwargs):
        order = Order.objects.get(id=self.kwargs.get("id"))
        order.delivery_status = self.request.POST.get("delivery_status")
        order.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))