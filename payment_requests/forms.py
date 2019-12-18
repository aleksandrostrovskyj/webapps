from django import forms
from django.core.exceptions import ValidationError

from .models import PaymentRequest

from datetime import date

class PaymentRequestForm(forms.ModelForm):
    class Meta:
        model = PaymentRequest
        exclude = ['request_date']

        widgets = {
            'payment_details': forms.Textarea(attrs={'rows': 2}),
            'form_w8ben_w9':  forms.Textarea(attrs={'rows': 2}),
        }

    def clean(self):
        cleaned_data = super().clean()

        #Validate planned payment date
        if cleaned_data['planned_payment_date'] <= date.today():
            raise ValidationError({'planned_payment_date': 'Planned Payment Date should be in the future.'})

        #Validate planned payment date
        fact_payment_date = cleaned_data['fact_payment_date']
        if fact_payment_date and fact_payment_date > date.today():
            raise ValidationError({'fact_payment_date': 'Fact Payment Date cannot be in the future.'})

        return cleaned_data


class UploadRequestForm(forms.Form):
    file_field = forms.FileField()
