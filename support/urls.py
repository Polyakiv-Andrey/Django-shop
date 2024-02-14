from django.urls import path

from support.views import ContactUsView

urlpatterns = [
    path('contact-us-form/', ContactUsView.as_view(), name="contact-us"),
]

app_name = "support"
