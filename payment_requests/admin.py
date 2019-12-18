from django.contrib import admin

# Register your models here.
from .models import PaymentRequest

admin.site.register(PaymentRequest)
