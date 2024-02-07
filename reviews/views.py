import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View

from basket.models import Goods
from orders.models import Order
from reviews.models import Reviews


class RateProductView(View):

    def get(self, request, *args, **kwargs):
        goods_id = self.kwargs.get("goods_id")
        order = get_object_or_404(Order, goods__id=goods_id)
        user_id = self.request.COOKIES.get("user_id")
        goods = Goods.objects.get(id=goods_id)
        try:
            review = Reviews.objects.get(
                goods_id=goods_id,
                user_id=user_id,
                order=order,
                product=goods.product.id,
            )
            rating = review.rating
        except Reviews.DoesNotExist:
            rating = None
        return JsonResponse({"rating": rating})

    def post(self, request, *args, **kwargs):
        goods_id = self.kwargs.get("goods_id")
        order = get_object_or_404(Order, goods__id=goods_id)
        user_id = self.request.COOKIES.get("user_id")
        goods = Goods.objects.get(id=goods_id)
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        rating = body_data.get("rating")

        review, created = Reviews.objects.get_or_create(
            goods_id=goods_id,
            user_id=user_id,
            order=order,
            product_id=goods.product.id,
        )
        if review.rating:
            return JsonResponse({"status": "Rating already set"})
        else:
            review.rating = rating
            review.save()
            return JsonResponse({"status": "Success"})


class CommentProductView(View):

    def get(self, request, *args, **kwargs):
        user_id = self.request.COOKIES.get("user_id")
        goods_id = self.kwargs.get("goods_id")
        order = get_object_or_404(Order, goods__id=goods_id)
        goods = Goods.objects.get(id=goods_id)
        try:
            review = Reviews.objects.get(
                goods_id=goods_id,
                user_id=user_id,
                order=order,
                product=goods.product.id,
            )
            comment = review.comment
        except Reviews.DoesNotExist:
            comment = None
        return JsonResponse({"comment": comment})

    def post(self, request, *args, **kwargs):
        user_id = self.request.COOKIES.get("user_id")
        goods_id = self.kwargs.get("goods_id")
        goods = Goods.objects.get(id=goods_id)
        order = get_object_or_404(Order, goods__id=goods_id)
        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)

        comment = body_data.get("comment")

        review, created = Reviews.objects.get_or_create(
            goods_id=goods_id,
            user_id=user_id,
            order=order,
            product_id=goods.product.id,
        )
        if len(comment) < 1:
            return JsonResponse({"status": "Failed"})
        else:
            review.comment = comment
            review.save()
            return JsonResponse({"status": "Success"})


class GetAverageRateOfProduct(View):

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get("product_id")
        reviews = Reviews.objects.filter(product_id=product_id)
        ratings = [review.rating for review in reviews if review.rating]
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        return JsonResponse({"avg_rating": avg_rating})


class GetCommentAmountForProduct(View):

    def get(self, request, *args, **kwargs):
        product_id = self.kwargs.get("product_id")
        reviews = Reviews.objects.filter(product_id=product_id)
        comments = [review.comment for review in reviews if review.comment]
        comments_amount = len(comments)
        return JsonResponse({"comments_amount": comments_amount})