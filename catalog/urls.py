from django.urls import path

from catalog.views import (
    ListCatalogItemView,
    DeleteCatalogView,
    CreateCatalogItemView,
    UpdateCatalogItemView,
)

urlpatterns = [
    path('catalog/list/<str:template_name>/', ListCatalogItemView.as_view(), name='catalog-list'),
    path('catalog-item-add/', CreateCatalogItemView.as_view(), name="catalog-item-add"),
    path('delete/<int:pk>/', DeleteCatalogView.as_view(), name='delete_catalog'),
    path('<int:pk>/update/', UpdateCatalogItemView.as_view(), name='update_catalog_item'),
]

app_name = "catalog"
