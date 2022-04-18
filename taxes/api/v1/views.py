import datetime

from django.db.models import Sum, Count
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response

from taxes.api.v1.serializers import PayableListSerializer, PayableSerializer, TransactionSerializer, TransactionSummarySerializer
from taxes.models import Payable, Transaction

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


class TransactionViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def list(self, request):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)
        self.validate_dates(start_date, end_date)
        queryset = (Transaction.objects.filter(payment_date__gte=start_date, payment_date__lte=end_date)
            .values('payment_date__date')
            .annotate(total=Sum('payment_import'), count=Count('payment_import'))
        )
        serializer = TransactionSummarySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def validate_dates(self, start_date: str, end_date: str):
        if not start_date or not end_date:
            raise serializers.ValidationError({'date_range': ['Please specify start date and end date']})
        try:
            start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
        except ValueError:
            raise serializers.ValidationError({'date_range': ['The start date format is invalid']})
        try:
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
        except ValueError:
            raise serializers.ValidationError({'date_range': ['The start date format is invalid']})
        if start_date > end_date:
            raise serializers.ValidationError({'date_range': ["Start date can't be greater than end date."]})
        