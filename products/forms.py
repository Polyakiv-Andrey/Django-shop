from django import forms
from django.forms.models import inlineformset_factory
from .models import Product, ProductImages, ProductAttribute, Discount


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'brand', 'description', 'catalog_item', 'price', 'inventory']


ProductImagesFormset = inlineformset_factory(
    Product,
    ProductImages,
    fields=('image', 'main', 'color', 'price'),
    extra=20,
    can_delete=True
)


ProductAttributeFormset = inlineformset_factory(
    Product,
    ProductAttribute,
    fields=('name', 'value', 'title'),
    extra=150,
    can_delete=True
)

DiscountFormset = inlineformset_factory(
    Product,
    Discount,
    fields=('percentage', 'start_date', 'end_date',),
    extra=1,
    can_delete=False
)
