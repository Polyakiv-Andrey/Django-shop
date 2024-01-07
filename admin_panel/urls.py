from django.urls import path

from .views import AdminPanelView

urlpatterns = [
    path('', AdminPanelView.as_view(), name="index"),
]

app_name = "admin_panel"
