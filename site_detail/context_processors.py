from .models import SiteDetail

def site_details(request):
    site, _ = SiteDetail.objects.get_or_create(id=1)
    return {'site': site}