from django.urls import path

from catalog.views import ListCatalogItemView, DeleteCatalogView

urlpatterns = [
    path('catalog/list/<str:template_name>/', ListCatalogItemView.as_view(), name='catalog-list'),
    path('delete/<int:pk>/', DeleteCatalogView.as_view(), name='delete_catalog'),
]

app_name = "catalog"
