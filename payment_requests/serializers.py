from rest_framework import serializers
from .models import PaymentRequest

from datetime import date

class PaymentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRequest
        fields = '__all__'

    def validate_planned_payment_date(self, value):
        if value < date.today():
            raise serializers.ValidationError('Planned Payment Date should be in the future.')
        return value
