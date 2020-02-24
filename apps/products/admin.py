from django.contrib import admin
from .models import (
    Product,
    Country
)

admin.site.register(Product)
admin.site.register(Country)
