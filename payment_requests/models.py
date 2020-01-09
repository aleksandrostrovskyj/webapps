from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import reverse

from .utils import *
# Create your models here.

class PaymentRequest(models.Model):
    request_date = models.DateField(auto_now_add=True, verbose_name='Created')
    payment_metod = models.CharField(
        max_length=2,
        choices=PaymentMethod.choices(),
        default=PaymentMethod.MANUAL,
        verbose_name='PayMethod'
    )
    department = models.CharField(max_length=10, verbose_name='Deprt-nt')
    subdivision = models.CharField(max_length=250, verbose_name='Division')
    user = models.CharField(max_length=250, verbose_name='User')
    payment_system = models.CharField(
        max_length=2,
        choices=PaymentSystem.choices(),
        verbose_name='PaySystem'
    )
    recipient = models.CharField(max_length=250, verbose_name='Recep.')
    requisits = models.CharField(max_length=999, verbose_name='Requsits')
    form_w8ben_w9 = models.CharField(max_length=250, blank=True, verbose_name='FormW8')
    payment_details = models.CharField(max_length=999, blank=True, verbose_name='Details')
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices(),
        verbose_name='Currency'
    )
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    planned_payment_date = models.DateField(verbose_name='Plan')
    compositions_of_payment_negotiations = models.CharField(verbose_name='Approver', max_length=10, blank=True)


    ceo = models.CharField(
        max_length=10,
        choices=Ceo.choices(),
        blank=True
    )
    fact_payment_date = models.DateField(blank=True, null=True, verbose_name='Fact')

    class Meta:
        ordering = ['id']
