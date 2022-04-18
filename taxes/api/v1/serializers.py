from rest_framework import serializers
from taxes.models import Payable, Transaction

class PayableListSerializer(serializers.ModelSerializer):
    """
    Serializer to list payables.
    Specifies some fields to show in the list and contains logic to exclude the field `service_type`.
    """
    class Meta:
        model = Payable
        fields = ['service_type', 'expiration_date', 'service_import', 'barcode']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        # Requirement indicates that the service_type field should be removed if it's used as a filter.
        request = self.context.get('request', None)
        if request is not None and request.query_params.get('service_type'):
            ret.pop('service_type')
        return ret
        

class PayableSerializer(serializers.ModelSerializer):
    """Serializer to create payables."""
    class Meta:
        model = Payable
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    """Serializer to create transactions."""
    class Meta:
        model = Transaction
        fields = '__all__'
    
    def validate(self, data):
        if data['payment_method'] != Transaction.CASH and not data['card_number']:
            raise serializers.ValidationError({'payment_method': ['The card number is required']})
        return super().validate(data)


class TransactionSummarySerializer(serializers.Serializer):
    """Serializer to summarise the transactions by day."""
    payment_date__date = serializers.DateField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    count = serializers.IntegerField()
    