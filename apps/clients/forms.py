from django import forms
from .models import Prefix, Country, Spouse, Client, Measurement, Company


class PrefixForm(forms.ModelForm):
    class Meta:
        model = Prefix
        fields = ['name']


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['code', 'name']


class SpouseForm(forms.ModelForm):
    class Meta:
        model = Spouse
        fields = ['prefix', 'name', 'birth_date',
                  'mobile_phone', 'measurement', 'wedding_date']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['prefix', 'name', 'birth_date', 'mobile_phone',
                  'measurement', 'gender', 'marital_status', 'spouse',
                  'tax_number', 'civil_id', 'passport_id', 'phone',
                  'other_phone_alternative', 'email', 'site', 'company',
                  'fax', 'address', 'mailing_list', 'postal_code', 'city',
                  'country', 'nib', 'notes', 'date_last_visit']


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
