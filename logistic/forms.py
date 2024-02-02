from django import forms
from django.forms import TextInput

from logistic.models import DeliveryDetail


class DeliveryDetailForm(forms.ModelForm):
    street_address = forms.CharField(widget=TextInput())

    class Meta:
        model = DeliveryDetail
        fields = [
            'user_id', 'first_name', 'last_name', 'email', 'phone',
            'street_address', 'city', 'state_province', 'postal_code', 'country'
        ]