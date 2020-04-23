from django import forms
from .models import Prefix, Country, Spouse, Client, Measurement, Company
from betterforms.multiform import MultiModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Fieldset, Layout, Submit


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
