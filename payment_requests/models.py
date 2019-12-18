from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import reverse

# Create your models here.

class PaymentRequest(models.Model):

    MANUAL = 'MN'
    AUTO = 'AU'
    SEMAUTO = 'SA'
    PAYMENT_METHOD_CHOICES = [
        (MANUAL, 'Manual'),
        (AUTO, 'Auto'),
        (SEMAUTO, 'Semi-automatic'),
    ]


    PRIVAT = 'PB'
    PAYPAL = 'PP'
    BANK_ACCOUNT = 'BA'
    PAYONEER = 'PO'
    CREDIT_CARD = 'CC'
    CASH = 'CH'
    BY_CHOICE = 'BC'
    PAYMENT_SYSTEM_CHOICES = [
        (PRIVAT, 'Privat 24'),
        (PAYPAL, 'PayPal'),
        (BANK_ACCOUNT, 'Bank Account'),
        (PAYONEER, 'Payoneer'),
        (CREDIT_CARD, 'Credit Card'),
        (CASH, 'Cash'),
        (BY_CHOICE, 'By choice'),
    ]


    UAH = 'UAH'
    USD = 'USD'
    EUR = 'EUR'
    GBP = 'GBP'
    RUB = 'RUB'
    CAD = 'CAD'
    PLN = 'PLN'
    CZK = 'CZK'
    CURRENCY_CHOICES = [
        (UAH, 'UAH'),
        (USD, 'USD'),
        (EUR, 'EUR'),
        (GBP, 'GBP'),
        (RUB, 'RUB'),
        (CAD, 'CAD'),
        (PLN, 'PLN'),
        (CZK, 'CZK'),
    ]


    YES = 'YES'
    NO = 'NO'
    ON_HOLD = 'OH'
    CANCELLED = 'CNC'
    CEO_CHOICES = [
        (YES, 'yes'),
        (NO, 'no'),
        (ON_HOLD, 'on hold'),
        (CANCELLED, 'cancelled'),
    ]

    request_date = models.DateField(auto_now_add=True)
    payment_metod = models.CharField(
        max_length=2,
        choices=PAYMENT_METHOD_CHOICES,
        default=MANUAL
    )
    department = models.CharField(max_length=10)
    subdivision = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    payment_system = models.CharField(
        max_length=2,
        choices=PAYMENT_SYSTEM_CHOICES
    )
    recipient = models.CharField(max_length=250)
    requisits = models.CharField(max_length=999)
    form_w8ben_w9 = models.CharField(max_length=250, blank=True)
    payment_details = models.CharField(max_length=999, blank=True)
    currency = models.CharField(
        max_length=3,
        choices=CURRENCY_CHOICES
    )
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    planned_payment_date = models.DateField()
    compositions_of_payment_negotiations = models.CharField(verbose_name='Approver', max_length=10, blank=True)


    ceo = models.CharField(
        max_length=10,
        choices=CEO_CHOICES,
        blank=True
    )
    fact_payment_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('payment_requests:pr_detail_url', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('payment_requests:pr_edit_url', kwargs = {'pk': self.id})

    def get_create_url(self):
        return reverse('payment_requests:pr_create_url')
