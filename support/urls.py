from django.urls import path

from support.views import ContactUsView, AdminSupportListView, SendSupportResponseView

urlpatterns = [
    path('contact-us-form/', ContactUsView.as_view(), name="contact-us"),
    path('admin-support/', AdminSupportListView.as_view(), name="admin-support"),
    path('send-support-response/<int:id>/', SendSupportResponseView.as_view(), name="send-support-response"),
]

app_name = "support"
