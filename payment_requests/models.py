from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import reverse

from .utils import *
# Create your models here.

class PaymentRequest(models.Model):
    request_date = models.DateField(auto_now_add=True)
    payment_metod = models.CharField(
        max_length=2,
        choices=PaymentMethod.choices(),
        default=PaymentMethod.MANUAL
    )
    department = models.CharField(max_length=10)
    subdivision = models.CharField(max_length=250)
    user = models.CharField(max_length=250)
    payment_system = models.CharField(
        max_length=2,
        choices=PaymentSystem.choices()
    )
    recipient = models.CharField(max_length=250)
    requisits = models.CharField(max_length=999)
    form_w8ben_w9 = models.CharField(max_length=250, blank=True)
    payment_details = models.CharField(max_length=999, blank=True)
    currency = models.CharField(
        max_length=3,
        choices=Currency.choices()
    )
    amount = models.DecimalField(max_digits=13, decimal_places=2)
    planned_payment_date = models.DateField()
    compositions_of_payment_negotiations = models.CharField(verbose_name='Approver', max_length=10, blank=True)


    ceo = models.CharField(
        max_length=10,
        choices=Ceo.choices(),
        blank=True
    )
    fact_payment_date = models.DateField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('payment_requests:pr_detail_url', kwargs={'pk': self.id})

    def get_edit_url(self):
        return reverse('payment_requests:pr_edit_url', kwargs = {'pk': self.id})

    def get_create_url(self):
        return reverse('payment_requests:pr_create_url')
