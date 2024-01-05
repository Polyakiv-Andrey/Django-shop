from django import forms

from catalog.models import CatalogItem


class CatalogItemForm(forms.ModelForm):

    class Meta:
        model = CatalogItem
        fields = ['name', 'image', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter item name'}),
            'image': forms.ClearableFileInput(attrs={'placeholder': 'Upload an image'}),
            'icon': forms.ClearableFileInput(attrs={'placeholder': 'Upload an icon'}),
        }
