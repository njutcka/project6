from django import forms

from catalog.models import Product, Version
from config import settings


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('name', 'description_product', 'price',)
        # exclude = ('is_active',)

    def clean(self):

        cleaned_data = super().clean()
        name = cleaned_data.get('name').lower()
        description = cleaned_data.get('description_product').lower()

        if name and any(word in name for word in settings.FORBIDDEN_WORDS):
            self.add_error('name', 'Недопустимое слово в названии продукта!')

        if description and any(word in description for word in settings.FORBIDDEN_WORDS):
            self.add_error('description_product', 'Недопустимое слово в описании продукта!')

        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name', 'number_version', 'current_version',)
