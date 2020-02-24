from django.shortcuts import render
from .models import Prefix, Country, Spouse, Client, Measurement, Company
from .forms import PrefixForm, CountryForm, SpouseForm, ClientForm, MeasurementForm, CompanyForm


def prefix_create_view(request):
    form = PrefixForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "clients/client_create.html", context)
