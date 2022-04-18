from rest_framework import viewsets, status
from rest_framework.response import Response

from taxes.api.v1.serializers import PayableListSerializer, PayableSerializer
from taxes.models import Payable

class PayableViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Payable.objects.filter(payment_status=Payable.PENDING)
        service_type = request.query_params.get('service_type')
        if service_type is not None:
            queryset = queryset.filter(service_type=service_type.upper())
        serializer = PayableListSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = PayableSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
