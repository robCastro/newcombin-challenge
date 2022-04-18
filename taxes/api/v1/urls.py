from django.urls import include, path
from rest_framework import routers

from taxes.api.v1.views import PayableViewSet

router = routers.DefaultRouter()
router.register(r'payables', PayableViewSet, basename='payable')

urlpatterns = [
    path('', include(router.urls)),
]
