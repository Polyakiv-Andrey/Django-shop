from django.shortcuts import render, redirect
from django.views import generic

from site_detail.models import SiteDetail


class EditSiteInfoView(generic.View):
    template_name = "adminPanel/site-info.html"

    def get(self, request, *args, **kwargs):
        site, created = SiteDetail.objects.get_or_create(id=1)
        context = {"site": site}
        return render(request=request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        site, created = SiteDetail.objects.get_or_create(id=1)
        for key, value in self.request.POST.items():
            if hasattr(site, key) and key not in ('logo', "about_us_image"):
                setattr(site, key, value)
        if 'logo' in request.FILES:
            site.logo = request.FILES['logo']
        if 'about_us_image' in request.FILES:
            site.about_us_image = request.FILES['about_us_image']
        site.save()
        return redirect('site_detail:edit-site-info')


class AboutUSView(generic.TemplateView):
    template_name = "shop/aboutUs.html"
