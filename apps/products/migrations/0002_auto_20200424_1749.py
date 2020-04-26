# Generated by Django 2.2 on 2020-04-24 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='country',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.Country'),
        ),
    ]
