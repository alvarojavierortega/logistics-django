from rest_framework import serializers
from .models import Carrier, Client, Package

'''Generic Serializer'''

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'


'''Detailed Serializers for carrier model'''

class CarrierSimplifiedClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id','name']

class CarrierPackageSerializer(serializers.ModelSerializer):
    owner = CarrierSimplifiedClientSerializer(read_only=True)
    class Meta:
        model = Package
        fields = ['owner','weight', 'size', 'origin_address', 'destination_address', 'delivery_status']

class DetailedCarrierSerializer(serializers.ModelSerializer):
    packages = CarrierPackageSerializer(many=True, read_only=True)

    class Meta:
        model = Carrier
        fields = '__all__'

'''Detailed serializers for client model'''

class ClientSimplifiedCarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id','name']


class ClientPackageSerializer(serializers.ModelSerializer):
    carrier = ClientSimplifiedCarrierSerializer(read_only=True)
    class Meta:
        model = Package
        fields = ['carrier','weight', 'size', 'origin_address', 'destination_address', 'delivery_status']


class DetailedClientSerializer(serializers.ModelSerializer):
    packages = ClientPackageSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = '__all__'






