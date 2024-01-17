from django import template
from django.shortcuts import get_object_or_404

from products.models import Product

register = template.Library()


@register.filter
def get_by_id(queryset, value):
    return get_object_or_404(Product, id=value)