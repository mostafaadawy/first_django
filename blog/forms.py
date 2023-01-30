from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title custom', widget=forms.TextInput(
        attrs={
            "placeholder": "HI Janna",
        }
    ))
    content = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            "placeholder": "HI Janna",
            "class": "new-class-name two",
            "id": "desc",
            "rows": 12,
            "cols": 120,
        }
    ))
    active = forms.BooleanField()

    class Meta:
        model = Article
        fields = [
            'title',
            'content',
            'active'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if len(title) < 4:
            raise forms.ValidationError("short")
        return title
