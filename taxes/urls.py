from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('taxes.api.v1.urls')),
]
