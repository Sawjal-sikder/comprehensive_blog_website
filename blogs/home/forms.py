from django import forms
from .models import Blog
from django_ckeditor_5.widgets import CKEditor5Widget


class BlogForm(forms.ModelForm):
    l_description = forms.CharField(widget=CKEditor5Widget(attrs={"class": "django_ckeditor_5"}))

    class Meta:
        model = Blog
        fields = '__all__'
