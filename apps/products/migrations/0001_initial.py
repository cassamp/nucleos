# Generated by Django 2.2 on 2020-04-23 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('nature', models.CharField(choices=[('P', 'Produto'), ('S', 'Serviço')], max_length=1)),
                ('category', models.CharField(choices=[('A', 'Produtos acabados e intermédios'), ('M', 'Mercadorias'), ('P', 'Matérias primas'), ('S', 'Sub-produtos desperdícios e refugos'), ('T', 'Produtos e trabalhos em curso')], max_length=1)),
                ('vat_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=15)),
                ('exemption_reason', models.CharField(choices=[('M01', 'Artigo 16.º n.º 6 alínea c) do CIVA'), ('M02', 'Artigo 6.º do Decreto‐Lei n.º 198/90, de 19 de Junho'), ('M03', 'Exigibilidade de caixa'), ('M04', 'Isento Artigo 13.º do CIVA'), ('M05', 'Isento Artigo 14.º do CIVA'), ('M06', 'Isento Artigo 15.º do CIVA'), ('M07', 'Isento Artigo 9.º do CIVA'), ('M08', 'IVA – Autoliquidação'), ('M09', 'IVA ‐ não confere direito a dedução'), ('M19', 'IVA – Regime de isenção'), ('M11', 'Regime particular do tabaco'), ('M12', 'Regime da margem de lucro – Agências de Viagens'), ('M13', 'Regime da margem de lucro – Bens em segunda mão'), ('M14', 'Regime da margem de lucro – Objetos de arte'), ('M15', 'Regime da margem de lucro – Objetos de coleção e antiguidades'), ('M16', 'Isento Artigo 14.º do RITI'), ('M99', 'Não sujeito; não tributado (ou similar)')], max_length=3)),
                ('pvp', models.DecimalField(decimal_places=2, default=False, max_digits=15)),
                ('country', models.ForeignKey(default='PT', on_delete=django.db.models.deletion.CASCADE, to='products.Country')),
            ],
        ),
    ]
