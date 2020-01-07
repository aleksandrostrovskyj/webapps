# Generated by Django 3.0.1 on 2020-01-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateField(auto_now_add=True)),
                ('payment_metod', models.CharField(choices=[('MN', 'Manual'), ('AU', 'Auto'), ('SA', 'Semi-automatic')], default='MN', max_length=2)),
                ('department', models.CharField(max_length=10)),
                ('subdivision', models.CharField(max_length=250)),
                ('user', models.CharField(max_length=250)),
                ('payment_system', models.CharField(choices=[('PB', 'Privat 24'), ('PP', 'PayPal'), ('BA', 'Bank Account'), ('PO', 'Payoneer'), ('CC', 'Credit Card'), ('CH', 'Cash'), ('BC', 'By choice')], max_length=2)),
                ('recipient', models.CharField(max_length=250)),
                ('requisits', models.CharField(max_length=999)),
                ('form_w8ben_w9', models.CharField(blank=True, max_length=250)),
                ('payment_details', models.CharField(blank=True, max_length=999)),
                ('currency', models.CharField(choices=[('UAH', 'UAH'), ('USD', 'USD'), ('EUR', 'EUR'), ('GBP', 'GBP'), ('RUB', 'RUB'), ('CAD', 'CAD'), ('PLN', 'PLN'), ('CZK', 'CZK')], max_length=3)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=13)),
                ('planned_payment_date', models.DateField()),
                ('compositions_of_payment_negotiations', models.CharField(blank=True, max_length=10, verbose_name='Approver')),
                ('ceo', models.CharField(blank=True, choices=[('YES', 'yes'), ('NO', 'no'), ('OH', 'on hold'), ('CNC', 'cancelled')], max_length=10)),
                ('fact_payment_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]