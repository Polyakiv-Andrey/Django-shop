from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic

from catalog.forms import CatalogItemForm
from catalog.models import CatalogItem


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
        return context


class CreateCatalogItemView(generic.CreateView):

    model = CatalogItem
    form_class = CatalogItemForm
    template_name = 'adminPanel/catalog/catalogItemForm.html'

    def form_valid(self, form):
        self.object = form.save()
        catalog_item_html = render_to_string('adminPanel/catalog/catalog-item.html', {'item': self.object})
        return JsonResponse({'status': 'success', 'html': catalog_item_html})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

