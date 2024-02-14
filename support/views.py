from django.shortcuts import render
from django.views import generic

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
