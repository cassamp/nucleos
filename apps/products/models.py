from django.db import models
# Create your models here.


class Country(models.Model):
    code = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name


class Product(models.Model):
    description = models.CharField(max_length=255)
    NATURE_CHOICES = [
        ('P', 'Produto'),
        ('S', 'Serviço')
    ]
    nature = models.CharField(max_length=1, choices=NATURE_CHOICES)
    CATEGORY_CHOICES = [
        ('A', 'Produtos acabados e intermédios'),
        ('M', 'Mercadorias'),
        ('P', 'Matérias primas'),
        ('S', 'Sub-produtos desperdícios e refugos'),
        ('T', 'Produtos e trabalhos em curso')
    ]
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    vat_rate = models.DecimalField(max_digits=15, decimal_places=2, blank=True)
    EXEMPTION_REASON_CHOICES = [
        ('M01', 'Artigo 16.º n.º 6 alínea c) do CIVA'),
        ('M02', 'Artigo 6.º do Decreto‐Lei n.º 198/90, de 19 de Junho'),
        ('M03', 'Exigibilidade de caixa'),
        ('M04', 'Isento Artigo 13.º do CIVA'),
        ('M05', 'Isento Artigo 14.º do CIVA'),
        ('M06', 'Isento Artigo 15.º do CIVA'),
        ('M07', 'Isento Artigo 9.º do CIVA'),
        ('M08', 'IVA – Autoliquidação'),
        ('M09', 'IVA ‐ não confere direito a dedução'),
        ('M19', 'IVA – Regime de isenção'),
        ('M11', 'Regime particular do tabaco'),
        ('M12', 'Regime da margem de lucro – Agências de Viagens'),
        ('M13', 'Regime da margem de lucro – Bens em segunda mão'),
        ('M14', 'Regime da margem de lucro – Objetos de arte'),
        ('M15', 'Regime da margem de lucro – Objetos de coleção e antiguidades'),
        ('M16', 'Isento Artigo 14.º do RITI'),
        ('M99', 'Não sujeito; não tributado (ou similar)')
    ]
    exemption_reason = models.CharField(
        max_length=3, choices=EXEMPTION_REASON_CHOICES)
    country = models.ForeignKey(
        'Country', on_delete=models.CASCADE, default='PT')
    units = models.PositiveIntegerField
    unit_weight = models.PositiveIntegerField
    pvp = models.DecimalField(max_digits=15, decimal_places=2, default=False)
