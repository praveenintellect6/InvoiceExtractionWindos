# Generated by Django 5.2.1 on 2025-06-11 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_columnmapping_column_supplier_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minvalue', models.IntegerField()),
                ('maxvalue', models.IntegerField()),
                ('profit', models.CharField(max_length=150)),
                ('selling_price_exc_gst', models.CharField(max_length=150)),
                ('gst', models.CharField(max_length=150)),
                ('selling_price_inc_gst', models.CharField(max_length=150)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.supplier')),
            ],
        ),
        migrations.DeleteModel(
            name='CalculationCase',
        ),
    ]
