from django.urls import path

from reviews.views import RateProductView, CommentProductView, GetAverageRateOfProduct, GetCommentAmountForProduct

urlpatterns = [
    path('rate-product/<int:goods_id>/', RateProductView.as_view(), name="rate-product"),
    path('comment-product/<int:goods_id>/', CommentProductView.as_view(), name="comment-product"),
    path('get-avg-rating/<int:product_id>/', GetAverageRateOfProduct.as_view(), name="average-rating"),
    path('get-comment-amount/<int:product_id>/', GetCommentAmountForProduct.as_view(), name="get-comment-amount"),
]

app_name = "reviews"
