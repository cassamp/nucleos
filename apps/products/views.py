from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, CreateView
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
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
