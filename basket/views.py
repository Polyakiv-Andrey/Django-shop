from django.views import generic

from basket.models import Basket, Goods


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
