from django.urls import reverse_lazy
from django.views import generic

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
