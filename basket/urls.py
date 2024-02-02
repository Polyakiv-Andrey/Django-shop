from django.urls import path

from basket.views import (
    BasketView,
    PlusItemFromBasketView,
    MinusItemFromBasketView,
    DeleteItemFromBasketView
)

urlpatterns = [
    path('', BasketView.as_view(), name="list"),
    path('plus-basket/<int:product_id>/', PlusItemFromBasketView.as_view(), name='plus_basket'),
    path('minus-basket/<int:product_id>/', MinusItemFromBasketView.as_view(), name='minus_basket'),
    path('delete-item-from-basket/<int:product_id>/', DeleteItemFromBasketView.as_view(), name="delete-item"),

]

app_name = "basket"
