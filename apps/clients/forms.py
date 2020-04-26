from django import forms
from .models import Prefix, Country, Spouse, Client, Measurement, Company
from betterforms.multiform import MultiModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Layout, Row, Submit


class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        exclude = ['measurement']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['spouse', 'measurement', 'company']


class MeasurementForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ['middle_finger_right', 'middle_finger_left',
                  'index_finger_right', 'index_finger_left',
                  'thumb_right', 'thumb_left', 'ring_finger_right',
                  'ring_finger_left', 'pinky_finger_right',
                  'pinky_finger_left', 'wrist_right',
                  'wrist_left', 'neck']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'phone',
                  'postal_code', 'city', 'country']


class ClientMultiForm(MultiModelForm):
    form_classes = {
        'client': ClientForm,
        'client_measurements': MeasurementForm,
        'spouse': SpouseForm,
        'spouse_measurements': MeasurementForm,
        'company': CompanyForm,
    }
    helper = FormHelper()
    helper.form_method = "POST"
    helper.add_input(Submit("newclient",
                            'Save', css_class='btn-success'))


class ClientInvoiceForm(forms.Form):
    client_id = forms.IntegerField(label='Client ID')
    product_id = forms.IntegerField(label='Product InvoiceXpressID')

    def clean(self):
        cleaned_data = super(ClientInvoiceForm, self).clean()
        client_id = cleaned_data.get('client_id')
        product_id = cleaned_data.get('product_id')
        if not client_id and not product_id:
            raise forms.ValidationError('Preencha o formulário!')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('client_id', css_class='form-group col-md-6 mb-0'),
                Column('product_id', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )
