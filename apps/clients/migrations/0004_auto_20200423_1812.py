# Generated by Django 2.2 on 2020-04-23 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20200423_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Company'),
        ),
        migrations.AlterField(
            model_name='client',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Country'),
        ),
        migrations.AlterField(
            model_name='client',
            name='prefix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Prefix'),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Country'),
        ),
        migrations.AlterField(
            model_name='spouse',
            name='prefix',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='clients.Prefix'),
        ),
    ]
