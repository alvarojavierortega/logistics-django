from rest_framework import viewsets, generics
from .models import Carrier, Client, Package
from .serializers import DetailedCarrierSerializer, DetailedClientSerializer, PackageSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CarrierLisAPIView(generics.ListAPIView):
    queryset = Carrier.objects.prefetch_related('packages')
    serializer_class = DetailedCarrierSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']


class ClientLisAPIView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = DetailedClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name']
    

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'carrier']


