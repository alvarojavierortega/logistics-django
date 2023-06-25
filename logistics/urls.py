from .views import CarrierLisAPIView, ClientLisAPIView, PackageViewSet
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('package', PackageViewSet, basename='packages')

urlpatterns = [
    path('', include(router.urls)),
    path('carrier/', CarrierLisAPIView.as_view(), name='carriers'),
    path('client/', ClientLisAPIView.as_view(), name='clients'),
]
