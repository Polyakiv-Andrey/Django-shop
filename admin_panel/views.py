from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic

from catalog.forms import CatalogItemForm
from catalog.models import CatalogItem


class AdminPanelView(generic.TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'adminPanel/index.html')


class CreateCatalogItemView(generic.CreateView):

    model = CatalogItem
    form_class = CatalogItemForm
    template_name = 'adminPanel/catalog/catalogItemForm.html'

    def form_valid(self, form):
        self.object = form.save()
        return JsonResponse({'status': 'success'})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

