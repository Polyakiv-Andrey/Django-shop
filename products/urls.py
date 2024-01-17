from django.urls import path

from products.views import CreateProductView, ProductDitailView, ProductCustomerList

urlpatterns = [
    path('create/', CreateProductView.as_view(), name="create_product"),
    path('detail/<int:pk>/', ProductDitailView.as_view(), name="product_detail"),
    path('product-list/', ProductCustomerList.as_view(), name="product-list")
]

app_name = "products"
