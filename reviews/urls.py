from django.urls import path

from reviews.views import RateProductView, CommentProductView

urlpatterns = [
    path('rate-product/<int:goods_id>/', RateProductView.as_view(), name="rate-product"),
    path('comment-product/<int:goods_id>/', CommentProductView.as_view(), name="comment-product"),
]

app_name = "reviews"
