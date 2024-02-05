from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from logistic.forms import DeliveryDetailForm
from logistic.models import DeliveryDetail


class CreateUpdateDetailDeliveryView(generic.View):
    template_name = 'shop/logistic_info.html'

    def get(self, request, *args, **kwargs):
        user_id = self.request.COOKIES.get("user_id")
        try:
            delivery_detail = DeliveryDetail.objects.get(user_id=user_id)
            form = DeliveryDetailForm(instance=delivery_detail)
        except DeliveryDetail.DoesNotExist:
            form = DeliveryDetailForm(initial={'user_id': user_id})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        user_id = request.COOKIES.get("user_id")
        try:
            delivery_detail = DeliveryDetail.objects.get(user_id=user_id)
            form = DeliveryDetailForm(request.POST, instance=delivery_detail)
        except DeliveryDetail.DoesNotExist:
            form = DeliveryDetailForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('payment:create-payment')

        return render(request, self.template_name, {'form': form})
