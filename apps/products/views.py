from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import ProductFilter
from .tables import ProductTable
from invoicexpress.services import ask_api


class ProductCreationView(LoginRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'products/create.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.save()
        unit_price = round((product.pvp / product.units), 1)
        result = ask_api('items.create', {
            'name': product.name,
            'description': product.description,
            'unit_price': unit_price,
        })
        return redirect('home')


class ProductListView(SingleTableMixin, FilterView):
    model = Product
    table_class = ProductTable
    template_name = 'products/list.html'
    filterset_class = ProductFilter

    def person_list(self, request):
        table = ProductTable(Product.objects.all())
        return render(request, "list.html", {
            "table": table
        })
