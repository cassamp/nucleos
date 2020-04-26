from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from .models import Client
from .forms import ClientForm, ClientMultiForm
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ClientFilter
from .tables import ClientTable
from invoicexpress.services import ask_api


class ClientCreationView(LoginRequiredMixin, CreateView):
    form_class = ClientMultiForm
    template_name = 'clients/create.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        client = form['client'].save(commit=False)
        spouse = form['spouse'].save(commit=False)
        client_measurements = form['client_measurements'].save()
        spouse_measurements = form['spouse_measurements'].save()
        company = form['company'].save()
        spouse.measurement = spouse_measurements
        spouse.save()
        client.measurement = client_measurements
        client.spouse = spouse
        client.company = company
        client.save()

        result = ask_api('clients.create', {
            'code': client.id,
            'name': client.name,
            'email': client.email,
            'fiscal_id': client.fiscal_number
        })

        return redirect('home')


class ClientListView(SingleTableMixin, FilterView):
    model = Client
    table_class = ClientTable
    template_name = 'clients/list.html'
    filterset_class = ClientFilter

    def person_list(self, request):
        table = ClientTable(Client.objects.all())
        return render(request, "list.html", {
            "table": table
        })


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
