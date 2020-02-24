from django.db import models

# Create your models here.


class Supplier(models.Model):
    name = models.CharField(max_length=200, blank=False)
    supplier_acronym = models.CharField(max_length=45, blank=False)
    email = models.EmailField(max_length=254, blank=True)
    tax_number = models.CharField(max_length=45, blank=False)
    phone = models.CharField(max_length=45, default=False)
    mobile_phone = models.CharField(max_length=45, default=False)
    other_phone_alternative = models.CharField(max_length=45, default=False)
    fax = models.CharField(max_length=45, default=False)
    site = models.CharField(max_length=200, default=False)
    MAILING_LIST_CHOICES = [
        ('S', 'Sim'),
        ('N', 'Não')
    ]
    mailing_list = models.CharField(
        max_length=1, choices=MAILING_LIST_CHOICES, default='Y')
    address = models.CharField(max_length=200, default=False)
    postal_code = models.CharField(max_length=45, default=False)
    city = models.CharField(max_length=45, default=False)
    contact = models.CharField(max_length=256, blank=False)
    product_counter = models.IntegerField(blank=1)
    service_counter = models.IntegerField(blank=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
