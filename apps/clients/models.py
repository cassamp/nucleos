from django.db import models


class Prefix(models.Model):
    name = models.CharField(primary_key=True, max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'prefixes'


class Country(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'countries'


class Spouse(models.Model):
    prefix = models.OneToOneField('Prefix', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    birth_date = models.DateField(blank=False)
    mobile_phone = models.CharField(max_length=45, blank=False)
    measurement = models.OneToOneField(
        'Measurement', on_delete=models.CASCADE, blank=True, null=True)
    wedding_date = models.DateField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    prefix = models.OneToOneField('Prefix', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    birth_date = models.DateField(blank=False)
    mobile_phone = models.CharField(max_length=45, blank=False)
    measurement = models.OneToOneField(
        'Measurement', on_delete=models.CASCADE, blank=True, null=True)
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('E', 'Empresa')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    MARITAL_STATUS_CHOICES = [
        ('1', 'Solteiro'),
        ('2', 'Divorciado'),
        ('3', 'Casado'),
        ('4', 'Viuvo')
    ]
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_STATUS_CHOICES)
    spouse = models.OneToOneField(
        'Spouse', on_delete=models.CASCADE, blank=True, null=True)
    tax_number = models.CharField(max_length=45)
    civil_id = models.CharField(max_length=45, blank=True)
    passport_id = models.CharField(max_length=45, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    other_phone_alternative = models.CharField(max_length=45, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    site = models.CharField(max_length=200, blank=True)
    company = models.OneToOneField(
        'Company', on_delete=models.CASCADE, blank=True, null=True)
    fax = models.CharField(max_length=45, blank=True)
    address = models.CharField(max_length=200, blank=True)
    MAILING_LIST_CHOICES = [
        ('S', 'Sim'),
        ('N', 'Não')
    ]
    mailing_list = models.CharField(max_length=1, choices=MAILING_LIST_CHOICES)
    postal_code = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, default='PT')
    nib = models.CharField(max_length=128, blank=True)
    notes = models.CharField(max_length=1024, blank=True)
    discount = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    date_last_visit = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    middle_finger_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    middle_finger_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    index_finger_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    index_finger_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    thumb_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    thumb_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    ring_finger_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    ring_finger_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    pinky_finger_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    pinky_finger_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    wrist_right = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    wrist_left = models.DecimalField(
        max_digits=15, decimal_places=2, blank=True)
    neck = models.DecimalField(max_digits=15, decimal_places=2, blank=True)


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=45, blank=True)
    postal_code = models.CharField(max_length=45, blank=True)
    city = models.CharField(max_length=45, blank=True)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, default='PT')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'
