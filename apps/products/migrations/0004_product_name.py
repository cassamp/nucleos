# Generated by Django 2.2 on 2020-04-26 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200425_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=9, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
