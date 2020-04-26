import django_tables2 as tables
from .models import Client


class ClientTable(tables.Table):
    class Meta:
        model = Client
        template_name = "django_tables2/bootstrap.html"
        fields = ['pk', 'name', 'email', 'fiscal_number']
