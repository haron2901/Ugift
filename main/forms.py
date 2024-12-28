from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['url', 'name', 'price', 'quantity_purchased', 'description', 'for_who',
                  'ozon_url', 'yandex_market_url', 'wildberries_url',
                  'ozon_price', 'yandex_market_price', 'wildberries_price']


    for_who = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Product.FOR_WHO_CHOICES,
    )
