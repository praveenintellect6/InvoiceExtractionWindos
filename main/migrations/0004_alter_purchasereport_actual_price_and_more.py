# Generated by Django 5.2.1 on 2025-06-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_datadownloaded_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasereport',
            name='actual_price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='gst',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='profit',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='purchase_count',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='selling_price_exc_gst',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='selling_price_inc_gst',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='total_count',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='total_price',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='purchasereport',
            name='trade_price',
            field=models.CharField(max_length=10),
        ),
    ]
