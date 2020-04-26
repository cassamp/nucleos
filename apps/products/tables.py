import django_tables2 as tables
from .models import Product


class ProductTable(tables.Table):
    class Meta:
        model = Product
