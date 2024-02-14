from django.db import transaction
from django.shortcuts import render, redirect
from django.views import generic

from django_shop import settings
from notifications.tasks import send_email_task
from support.models import SupportRequest


class ContactUsView(generic.View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="shop/support.html")

    def post(self, request, *args, **kwargs):

        if SupportRequest.objects.filter(
                email=self.request.POST.get("email"),
                topic=self.request.POST.get("topic"),
                name=self.request.POST.get("name"),
                payload=self.request.POST.get("payload"),
        ).exists():
            context = {"status": "Failed"}
        else:
            SupportRequest.objects.create(
                name=self.request.POST.get("name"),
                email=self.request.POST.get("email"),
                topic=self.request.POST.get("topic"),
                payload=self.request.POST.get("payload"),
            )
            context = {"status": "Success"}
        return render(request=request, template_name="shop/support.html", context=context)


class AdminSupportListView(generic.ListView):
    model = SupportRequest
    queryset = SupportRequest.objects.all().order_by("response_send")
    paginate_by = 10
    template_name = "adminPanel/supportPage.html"


class SendSupportResponseView(generic.View):

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            support_id = self.kwargs.get("id")
            support = SupportRequest.objects.get(id=support_id)
            support.response_send = True
            support.response = self.request.POST.get("response")
            support.save()
            send_email_task.delay(settings.SUPPORT_RESPONSE, {"data": support.response}, support.email)

        return redirect('support:admin-support')