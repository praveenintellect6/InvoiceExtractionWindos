# Generated by Django 5.2.1 on 2025-06-16 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_invoiceinfo_mailsubject_invoiceinfo_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrappedDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maildate', models.DateField()),
            ],
        ),
    ]
