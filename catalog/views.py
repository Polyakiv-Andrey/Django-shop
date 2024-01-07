from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views import generic

from catalog.forms import CatalogItemForm
from catalog.models import CatalogItem


class ListCatalogItemView(generic.ListView):
    model = CatalogItem
    paginate_by = 15

    def get_template_names(self):
        template_name = self.kwargs.get('template_name')
        return [template_name]


class DeleteCatalogView(generic.DeleteView):
    model = CatalogItem
    success_url = reverse_lazy('admin_panel:index')


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


class UpdateCatalogItemView(generic.UpdateView):
    model = CatalogItem
    form_class = CatalogItemForm
    template_name = 'adminPanel/catalog/catalogItemUpdateForm.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(CatalogItem, pk=self.kwargs.get('pk'))
        return obj

    def form_valid(self, form):
        self.object = form.save()
        catalog_item_html = render_to_string('adminPanel/catalog/catalog-item.html', {'item': self.object})
        return JsonResponse({'status': 'success', 'html': catalog_item_html})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)