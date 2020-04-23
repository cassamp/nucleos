from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, CreateView
from .forms import SignUpForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'users/home.html'
    login_url = reverse_lazy('login')


class SignUpView(LoginRequiredMixin, CreateView):
    form_class = SignUpForm
    template_name = 'users/register.html'
    login_url = reverse_lazy('login')
