from django.core.exceptions import FieldError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView

from catalog.models import CatalogItem
from products.forms import *
from .models import Product


class CreateProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'adminPanel/products/productItemForm.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        counter = 0
        if self.request.POST:
            data['images'] = ProductImagesFormset(self.request.POST, self.request.FILES, prefix='images')
            data['attributes'] = ProductAttributeFormset(self.request.POST, prefix='attributes')
            data['discounts'] = DiscountFormset(self.request.POST, prefix='discounts')
        else:
            data['images'] = ProductImagesFormset(prefix='images')
            data['attributes'] = ProductAttributeFormset(prefix='attributes')
            data['discounts'] = DiscountFormset(prefix='discounts')
        data['images_empty_form'] = ProductImagesFormset(prefix='images', queryset=ProductImages.objects.none())[0]
        data['attributes_empty_form'] = ProductAttributeFormset(prefix='attributes', queryset=ProductAttribute.objects.none())[0]
        data['discounts_empty_form'] = DiscountFormset(prefix='discounts', queryset=Discount.objects.none())[0]
        data["counter"] = counter
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        images = context['images']
        attributes = context['attributes']
        discounts = context['discounts']

        self.object = form.save()

        if images.is_valid():
            images.instance = self.object
            images.save()

        if attributes.is_valid():
            attributes.instance = self.object
            attributes.save()

        if discounts.is_valid():
            discounts.instance = self.object
            discounts.save()

        catalog_item_html = render_to_string('adminPanel/catalog/catalog-item.html', {'item': self.object})
        return JsonResponse({'status': 'success', 'html': catalog_item_html})

    def form_invalid(self, form):
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)


class ProductDitailView(generic.DetailView):
    model = Product
    template_name = "adminPanel/products/product-detail.html"


class ProductCustomerList(generic.TemplateView):
    template_name = 'shop/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCustomerList, self).get_context_data(**kwargs)
        context["catalog_items"] = CatalogItem.objects.all()
        products = Product.objects.all().order_by('-inventory')
        filter_params = self.request.GET
        filter_q = Q()
        for key, value in filter_params.items():
            if key == "q":
                continue
            filter_q &= Q(**{key: value})
            try:
                products = products.filter(filter_q)
            except FieldError as e:
                print(e)
                continue
        product_filter = self.request.GET.get("q")
        if product_filter:
            products = products.filter(name__icontains=product_filter)
        paginator = Paginator(products, 12)
        page = self.request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context["products"] = products

        return context
