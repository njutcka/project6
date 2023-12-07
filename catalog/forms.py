from django import forms

from catalog.models import Product, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта',
                   'биржа', 'дешево', 'бесплатно', 'обман',
                   'полиция', 'радар'
                   ]

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        #fields = '__all__'
        fields = ('name', 'description_product', 'price',)
        #exclude = ('is_active',)

        def clean_name(self):
            cleaned_name = self.cleaned_data['name']
            cleaned_description = self.cleaned_data['description_product']
            for obj in FORBIDDEN_WORDS:
                if obj in cleaned_name:
                    raise forms.ValidationError("Недопустимое название продукта")
                if obj in cleaned_description:
                    raise forms.ValidationError("Недопустимое описание продукта")

            return cleaned_name


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'name', 'number_version', 'current_version',)

