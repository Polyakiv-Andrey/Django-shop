import json

import stripe
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import generic

from basket.models import Basket
from django_shop import settings
from django_shop.settings import STRIPE_PUBLIC_KEY
from logistic.models import DeliveryDetail
from orders.models import Order
from payment.models import Payments
from products.models import Product
from site_detail.models import SiteDetail

site_details, created = SiteDetail.objects.get_or_create(id=1)
if site_details.stripe_private_key != "None":
    stripe.api_key = site_details.stripe_private_key
else:
    stripe.api_key = settings.STRIPE_SECRET_KEY


class CreatePaymentAPIView(generic.View):
    template_name = "shop/payment.html"

    def get(self, request, *args, **kwargs):
        site_details, created = SiteDetail.objects.get_or_create(id=1)
        if site_details.stripe_public_key != "None":
            context = {"stripe_public_key": site_details.stripe_public_key}
        else:
            context = {"stripe_public_key": STRIPE_PUBLIC_KEY}
        try:
            basket = Basket.objects.get(user_id=self.request.COOKIES.get("user_id"))
        except Basket.DoesNotExist:
            return reverse_lazy("basket:list")
        context["basket"] = basket
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        user_id = self.request.COOKIES.get("user_id")
        data = json.loads(request.body.decode('utf-8'))
        payment_method_id = data.get('payment_method_id')
        try:
            site_detail = SiteDetail.objects.get(id=1)
            site_currency = site_detail.currency.lower()
            if site_currency == "uan":
                site_currency = "uah"
            if site_currency == "euro":
                site_currency = "eur"
        except SiteDetail.DoesNotExist:
            site_currency = 'usd'
        try:
            basket = Basket.objects.get(user_id=user_id)
        except Basket.DoesNotExist:
            return redirect("basket:list")
        try:
            delivery_info = DeliveryDetail.objects.get(user_id=user_id)
        except DeliveryDetail.DoesNotExist:
            return JsonResponse(
                {
                    'message': 'Payment not confirmed',
                    'redirect_url': reverse('logistic:create-update-delivery-ditail')
                }
            )
        except DeliveryDetail.MultipleObjectsReturned:
            delivery_info = DeliveryDetail.objects.filter(user_id=user_id).last()

        payment_amount = int(basket.get_basket_total_price * 100)

        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=payment_amount,
                currency=site_currency,
                confirm=True,
                payment_method=payment_method_id,
                return_url=request.build_absolute_uri(reverse('home')),
            )

        except stripe.error.CardError as e:
            return JsonResponse({'message': str(e)})

        if payment_intent.status == 'succeeded':
            order = Order.objects.create(
                delivery_status="created",
                delivery_info=delivery_info,
                user_id=user_id,
                data_created=timezone.now()
            )
            Payments.objects.create(
                amount=payment_amount // 100,
                currency=site_currency,
                delivery_ditail=delivery_info,
                order=order,
                transaction_status="success",
                data_created=timezone.now()
            )

            for goods in basket.goods.all():
                order.goods.add(goods)
                product = Product.objects.get(goods=goods)
                product.inventory -= goods.amount
                product.save()

            order.save()
            basket.goods.clear()
            basket.save()

            response_data = {'message': 'Payment successful', 'redirect_url': reverse('orders:user-order-list')}
            response = JsonResponse(response_data)

            for cookie_name in list(request.COOKIES.keys()):
                if cookie_name.startswith('basket'):
                    response.delete_cookie(cookie_name)

            return response
        else:
            return JsonResponse({'message': 'Payment not confirmed'})

        # 1)Произвести оплату
        # 2)Создать заказ
        # 3)Удалить все из корзины
        # 4)Удалить кукисы про товар
        # 5)Отправить письмо менеджеру на почту
        # 6)Перевести пользователя на страницу с заказами
