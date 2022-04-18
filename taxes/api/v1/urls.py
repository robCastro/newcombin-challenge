from django.urls import include, path
from rest_framework import routers

from taxes.api.v1.views import PayableViewSet, TransactionViewSet

router = routers.DefaultRouter()
router.register(r'payables', PayableViewSet, basename='payable')
router.register(r'transactions', TransactionViewSet, basename='transaction')

urlpatterns = [
    path('', include(router.urls)),
]
