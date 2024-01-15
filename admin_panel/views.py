from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic

from catalog.models import CatalogItem
from products.models import Product


class AdminPanelView(generic.TemplateView):
    template_name = 'adminPanel/index.html'

    def get_context_data(self, **kwargs):
        context = super(AdminPanelView, self).get_context_data(**kwargs)
        catalog_items_list = CatalogItem.objects.all().order_by('-id')
        paginator = Paginator(catalog_items_list, 11)
        page = self.request.GET.get('page')

        try:
            catalog_items = paginator.page(page)
        except PageNotAnInteger:
            catalog_items = paginator.page(1)
        except EmptyPage:
            catalog_items = paginator.page(paginator.num_pages)

        context['catalog_items'] = catalog_items
        product_filter = self.request.GET.get("q")
        product_items_list = Product.objects.all().order_by('-id').filter(name__contains=product_filter)
        paginator = Paginator(product_items_list, 11)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products
        return context


