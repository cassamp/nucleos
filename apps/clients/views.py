from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from .models import Client
from .forms import ClientForm, ClientMultiForm


class ClientCreationView(LoginRequiredMixin, CreateView):
    form_class = ClientMultiForm
    success_url = reverse_lazy('home')
    template_name = 'clients/create.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        client = form['client'].save()
        spouse = form['spouse'].save(commit=False)
        client_measurements = form['client_measurements'].save(commit=False)
        spouse_measurements = form['spouse_measurements'].save(commit=False)
        company = form['company'].save(commit=False)
        spouse.measurements = spouse_measurements
        client.spouse = spouse
        client.measurements = client_measurements
        client.company = company
        spouse.save()
        client_measurements.save()
        spouse_measurements.save()
        company.save()
        return redirect(self.get_success_url())


""" class ClientCreationView(UpdateView):
    model = Client
    form_class = ClientMultiForm
    success_url = reverse_lazy('home')

    def get_form_kwargs(self):
        kwargs = super(ClientCreationView, self).get_form_kwargs()
        kwargs.update(instance={
            'client': self.object,
            'spouse': self.object.spouse,
            'company': self.object.company,
            'client_measurements': self.object.measurements,
            'spouse_measurements': self.object.spouse.measurements,
        })
        return kwargs
 """
