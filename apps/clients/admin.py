from django.contrib import admin
from .models import (
    Prefix,
    Spouse,
    Client,
    Measurement,
    Country,
    Company)

admin.site.register(Prefix)
admin.site.register(Spouse)
admin.site.register(Client)
admin.site.register(Measurement)
admin.site.register(Country)
admin.site.register(Company)
