from .views import UpdateDeliveryStatusApiView, AssignCarrierApiView
from django.urls import path

urlpatterns = [
    path('package/<int:package_id>/status/<str:delivery_status>', UpdateDeliveryStatusApiView.as_view(), name='dummy_update_status'),
    path('package/<int:package_id>/carrier/<int:carrier_id>', AssignCarrierApiView.as_view(), name='dummy_update_status'),
]
