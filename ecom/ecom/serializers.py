from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView

from ecom.models import User, ShippingAddress


class CreateShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = ["street", "city", "state", "zipcode", "country"]

class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"

class UserSerializer(ModelSerializer):
    shipping_addresses = ShippingAddressSerializer(many=True, read_only=True)
    default_shipping_address = ShippingAddressSerializer(read_only=True)
    class Meta:
        model = User
        fields = "__all__"

class SetDefaultShippingAddress(APIView):

    def patch(self, request, user_id, address_id):
        user =get_object_or_404(User, pk=user_id)
        address = get_object_or_404(ShippingAddress, user_id=user_id, pk=user_id)
        user.save()

        return Response(
            UserSerializer(user), status=status.HTTP_200_OK
        )
