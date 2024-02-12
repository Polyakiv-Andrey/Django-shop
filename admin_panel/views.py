from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils.dateparse import parse_datetime
from django.views import generic

from catalog.models import CatalogItem
from products.models import Product, ProductImages, Discount, ProductAttribute


class AdminPanelView(LoginRequiredMixin, generic.TemplateView):
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
        product_items_list = Product.objects.all().order_by('-id')
        if product_filter:
            product_items_list = product_items_list.filter(name__contains=product_filter)
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


class AdminProductDetailView(generic.View):
    template_name = "adminPanel/products/product-detail.html"

    def get(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        context = {"product": product}
        return render(template_name=self.template_name, request=requests, context=context)

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        context = {"product": product}
        for key, value in requests.POST.items():
            if hasattr(product, key):
                setattr(product, key, value)
        product.save()
        return render(template_name=self.template_name, request=requests, context=context)


class SetMeinProductPhotoView(generic.View):

    def post(self, requests, *args, **kwargs):

        image_id = self.kwargs.get("pk")
        product = Product.objects.get(images__id=image_id)
        for image in product.images.all():
            if image_id == image.id:
                image.main = True
            else:
                image.main = False
            image.save()
        return HttpResponseRedirect(reverse('admin_panel:product-detail', args=[product.pk]))


class DeleteProductPhotoView(generic.View):

    def post(self, requests, *args, **kwargs):
        image_id = self.kwargs.get("pk")
        product = Product.objects.get(images__id=image_id)
        ProductImages.objects.filter(id=image_id).delete()
        return HttpResponseRedirect(reverse('admin_panel:product-detail', args=[product.pk]))


class CreateProductPhotoView(generic.View):

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        image = self.request.FILES.get("image")
        if image:
            if product.images.all().count() == 0:
                ProductImages.objects.create(product=product, image=image, main=True)
            else:
                ProductImages.objects.create(product=product, image=image)
        return HttpResponseRedirect(reverse('admin_panel:product-detail', args=[product.pk]))


class CreateUpdateDiscountView(generic.View):

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs.get("pk"))
        discount = Discount.objects.filter(product=product).first()
        percentage = requests.POST.get("percentage")
        if percentage and not discount:
            discount = Discount.objects.create(product=product, percentage=percentage)
        for key, value in requests.POST.items():
            if hasattr(discount, key):
                if isinstance(getattr(discount, key), datetime):
                    parsed_value = parse_datetime(value)
                    if parsed_value is not None:
                        setattr(discount, key, parsed_value)
                else:
                    setattr(discount, key, value)
        discount.save()
        return HttpResponseRedirect(reverse('admin_panel:product-detail', args=[product.pk]))


class DeleteDiscountView(generic.View):

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        Discount.objects.filter(product=product).delete()
        return HttpResponseRedirect(reverse('admin_panel:product-detail', args=[product.pk]))


class DeleteProductView(generic.View):

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        product.delete()
        return HttpResponseRedirect(reverse('admin_panel:index'))


class CreateProductPropertyView(generic.View):

    def post(self, requests, *args, **kwargs):
        product = get_object_or_404(Product, id=self.kwargs.get("pk"))
        if self.request.POST.get("name"):
            ProductAttribute.objects.create(
                product=product,
                name=self.request.POST.get("name"),
                value=self.request.POST.get("value"),
                title=True if self.request.POST.get("title") else False,
            )
        url = reverse('admin_panel:product-detail', args=[product.pk]) + '#createPropertyProd'
        return HttpResponseRedirect(url)


class UpdateProductPropertyView(generic.View):

    def post(self, requests, *args, **kwargs):
        product_property = get_object_or_404(ProductAttribute, id=self.kwargs.get("pk"))
        product = Product.objects.get(attributes=product_property)
        setattr(product_property, "title", False)
        for key, value in requests.POST.items():
            if hasattr(product_property, key):
                if key != "title":
                    setattr(product_property, key, value)
                else:
                    if value == "on":
                        setattr(product_property, key, True)
        product_property.save()

        url = reverse('admin_panel:product-detail', args=[product.pk]) + '#property' + str(product_property.id)
        return HttpResponseRedirect(url)


class DeleteProductPropertyView(generic.View):

    def post(self, requests, *args, **kwargs):
        product_property = get_object_or_404(ProductAttribute, id=self.kwargs.get("pk"))
        product = Product.objects.get(attributes=product_property)
        product_property.delete()
        url = reverse('admin_panel:product-detail', args=[product.pk]) + '#createPropertyProd'
        return HttpResponseRedirect(url)


class MoveUpProductPropertyView(generic.View):

    def post(self, requests, *args, **kwargs):
        product_property = get_object_or_404(ProductAttribute, id=self.kwargs.get("pk"))
        product = Product.objects.get(attributes=product_property)
        attributes = ProductAttribute.objects.filter(product=product).exclude(id__gte=product_property.id)
        attributes_id = []
        for attribute in attributes:
            attributes_id.append(attribute.id)
        if attributes_id:
            max_attributes_id = max(attributes_id)
            attribute_max_id = ProductAttribute.objects.get(id=max_attributes_id)
            attribute_max_id.id, product_property.id = product_property.id, attribute_max_id.id
            attribute_max_id.save()
            product_property.save()
        url = reverse('admin_panel:product-detail', args=[product.pk]) + '#property' + str(product_property.id)
        return HttpResponseRedirect(url)


class MoveDownProductPropertyView(generic.View):

    def post(self, requests, *args, **kwargs):
        product_property = get_object_or_404(ProductAttribute, id=self.kwargs.get("pk"))
        product = Product.objects.get(attributes=product_property)
        attributes = ProductAttribute.objects.filter(product=product).exclude(id__lte=product_property.id)
        attributes_id = []
        for attribute in attributes:
            attributes_id.append(attribute.id)
        if attributes_id:
            min_attributes_id = min(attributes_id)
            attribute_min_id = ProductAttribute.objects.get(id=min_attributes_id)
            attribute_min_id.id, product_property.id = product_property.id, attribute_min_id.id
            attribute_min_id.save()
            product_property.save()
        url = reverse('admin_panel:product-detail', args=[product.pk]) + '#property' + str(product_property.id)
        return HttpResponseRedirect(url)

