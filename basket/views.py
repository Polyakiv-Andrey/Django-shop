from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.views.decorators.http import require_POST

from basket.models import Basket, Goods
from products.models import Product


class BasketView(generic.TemplateView):
    template_name = "shop/basket.html"

    def get_context_data(self, **kwargs):
        context = super(BasketView, self).get_context_data(**kwargs)
        user_id = self.request.COOKIES.get("user_id")

        basket, created = Basket.objects.get_or_create(user_id=user_id)
        for prev_goods in basket.goods.all():
            prev_goods.delete()
        for key, value in self.request.COOKIES.items():
            if key.startswith("basket"):
                product_id = key.split("_")[1]
                goods = Goods.objects.create(
                    product_id=product_id,
                    amount=value
                )
                basket.goods.add(goods)

        context["basket"] = basket
        return context


class PlusItemFromBasketView(generic.View):

    def update_cookie(self, response, product_id):
        for key, value in self.request.COOKIES.items():
            try:
                if key.startswith(f'basket_{product_id}'):
                    response.set_cookie(key, str(int(value) + 1))
            except ValueError as e:
                print(e)

    def get(self, request, product_id):
        user = self.request.COOKIES.get("user_id")
        basket = Basket.objects.get(user_id=user)

        with transaction.atomic():
            good = Goods.objects.get(basket=basket, product_id=product_id)
            good.amount += 1
            good.save()
            response = redirect(request.META.get('HTTP_REFERER', '/'))
            self.update_cookie(response, product_id)

        return response


class MinusItemFromBasketView(generic.View):

    def update_cookie(self, response, product_id):
        for key, value in self.request.COOKIES.items():
            try:
                if key.startswith(f'basket_{product_id}'):
                    response.set_cookie(key, str(int(value) - 1))
            except ValueError as e:
                print(e)

    def get(self, request, product_id):
        user = self.request.COOKIES.get("user_id")
        basket = Basket.objects.get(user_id=user)

        with transaction.atomic():
            good = Goods.objects.get(basket=basket, product_id=product_id)
            response = redirect(request.META.get('HTTP_REFERER', '/'))
            if good.amount > 1:
                good.amount -= 1
                good.save()
                self.update_cookie(response, product_id)
        return response


class DeleteItemFromBasketView(generic.View):

    def update_cookie(self, response, product_id):
        for key, value in self.request.COOKIES.items():
            try:
                if key.startswith(f'basket_{product_id}'):
                    response.delete_cookie(key)
            except ValueError as e:
                print(e)

    def post(self, request, product_id):
        user = self.request.COOKIES.get("user_id")
        basket = Basket.objects.get(user_id=user)

        with transaction.atomic():
            good = Goods.objects.filter(basket=basket, product_id=product_id).delete()
            response = redirect(request.META.get('HTTP_REFERER', '/'))
            self.update_cookie(response, product_id)
        return response
