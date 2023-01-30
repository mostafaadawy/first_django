from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField(label='Title custom', widget=forms.TextInput(
        attrs={
            "placeholder": "HI Janna",
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            "placeholder": "HI Janna",
            "class": "new-class-name two",
            "id": "desc",
            "rows": 12,
            "cols": 120,

        }
    ))
    price = forms.DecimalField(initial=155.5)
