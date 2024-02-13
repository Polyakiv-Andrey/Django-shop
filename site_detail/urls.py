from django.urls import path

from site_detail.views import EditSiteInfoView, AboutUSView

urlpatterns = [
    path('edit-site-info/', EditSiteInfoView.as_view(), name="edit-site-info"),
    path("about-us/", AboutUSView.as_view(), name="about_us")
]

app_name = "site_detail"
