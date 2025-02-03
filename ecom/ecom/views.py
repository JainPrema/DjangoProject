from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import ShippingAddress, User
from .serializers import UserSerializer, ShippingAddressSerializer
from .serializers import CreateShippingAddressSerializer

class UserListCreateAPIView(APIView):
    def get(self,request):
        users = User.objects.all().prefetch_related('shipping_addresses').select_related('default_shipping_address')
        return Response(
            UserSerializer(users, many=True).data
        )

    def post(self,request):
        serialized = UserSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ShippingAddressListCreateAPIView(APIView):
    serializer_class = CreateShippingAddressSerializer
    def post(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        serialized = CreateShippingAddressSerializer(data=request.data)

        if not serialized.is_valid():
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

        shipping_address = ShippingAddress(
            street=serialized.validated_data['street'],
            city=serialized.validated_data['city'],
            state=serialized.validated_data['state'],
            zipcode=serialized.validated_data['zipcode'],
            country=serialized.validated_data['country'],
            user=user
        )
        shipping_address.save()
        return Response(ShippingAddressSerializer(
            shipping_address
        ).data, status=status.HTTP_201_CREATED)



