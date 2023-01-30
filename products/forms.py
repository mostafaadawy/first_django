from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
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

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "mos" in title:
            raise forms.ValidationError("this is not contains mos")
        if len(title) < 4:
            raise forms.ValidationError("short")
        return title


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
