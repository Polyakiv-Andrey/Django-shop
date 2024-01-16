from django.urls import path

from products.views import CreateProductView, ProductDitailView

urlpatterns = [
    path('create/', CreateProductView.as_view(), name="create_product"),
    path('detail/<int:pk>/', ProductDitailView.as_view(), name="product_detail"),
]

app_name = "products"
