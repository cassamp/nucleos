import django_filters
from .models import Client


class ClientFilter(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'fiscal_number']
