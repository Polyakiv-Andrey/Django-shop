from django.urls import path

from .views import AdminPanelView, CreateCatalogItemView

urlpatterns = [
    path('', AdminPanelView.as_view(), name="index"),
    path('catalog-item-add/', CreateCatalogItemView.as_view(), name="catalog-item-add"),
]

app_name = "admin_panel"
