from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    helper = FormHelper()
    helper.form_method = "POST"
    helper.add_input(Submit("newproduct",
                            'Save', css_class='btn-success'))
