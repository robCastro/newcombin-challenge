from rest_framework import serializers
from taxes.models import Payable

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