from rest_framework.views import APIView
from rest_framework.response import Response
from .dependency.logistics import logistics 
from typing import Literal
from rest_framework import status

class UpdateDeliveryStatusApiView(APIView):

    def get(self, request, package_id:int, delivery_status: Literal["Shipped", "Delivered", "Canceled"]):
        answer, status_code = logistics.update_package(package_id, delivery_status=delivery_status)
        if status_code == 200:
            return Response(answer, status=status.HTTP_200_OK)
        return Response(answer, status=status.HTTP_400_BAD_REQUEST)
    

class AssignCarrierApiView(APIView):

    def get(self, request, package_id:int, carrier_id: int):
        answer, status_code = logistics.update_package(package_id, carrier_id=carrier_id)
        if status_code == 200:
            return Response(answer, status=status.HTTP_200_OK)
        return Response(answer, status=status.HTTP_400_BAD_REQUEST)
    
    