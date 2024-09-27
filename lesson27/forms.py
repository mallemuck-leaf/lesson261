from django import forms
from .models import Product


class ProductForm(forms.Form):
    name = forms.CharField(max_length=30, required=True)
    price = forms.DecimalField(max_digits=11, decimal_places=2, required=True)

    class Meta:
        model = Product
