from django.urls import path

from .views import AdminPanelView, AdminProductDetailView, SetMeinProductPhotoView, DeleteProductPhotoView, \
    CreateProductPhotoView, CreateUpdateDiscountView, DeleteDiscountView, DeleteProductView, CreateProductPropertyView, \
    UpdateProductPropertyView, DeleteProductPropertyView, MoveUpProductPropertyView, MoveDownProductPropertyView

urlpatterns = [
    path('', AdminPanelView.as_view(), name="index"),
    path('product/<int:pk>/', AdminProductDetailView.as_view(), name="product-detail"),
    path("main-image/<int:pk>/", SetMeinProductPhotoView.as_view(), name="main-photo"),
    path('delete-image/<int:pk>/', DeleteProductPhotoView.as_view(), name="delete-photo"),
    path("create-photo/<int:pk>/", CreateProductPhotoView.as_view(), name="create-photo"),
    path("discount/<int:pk>/", CreateUpdateDiscountView.as_view(), name="discount"),
    path("delete-discount/<int:pk>/", DeleteDiscountView.as_view(), name="delete-discount"),
    path("delete-product/<int:pk>/", DeleteProductView.as_view(), name="delete-product"),
    path("create-property/<int:pk>/", CreateProductPropertyView.as_view(), name="create-property"),
    path("update-property/<int:pk>/", UpdateProductPropertyView.as_view(), name="update-property"),
    path("delete-property/<int:pk>/", DeleteProductPropertyView.as_view(), name="delete-property"),
    path("move-up-property/<int:pk>/", MoveUpProductPropertyView.as_view(), name="move-up-property"),
    path("move-down-property/<int:pk>/", MoveDownProductPropertyView.as_view(), name="move-down-property")
]

app_name = "admin_panel"
