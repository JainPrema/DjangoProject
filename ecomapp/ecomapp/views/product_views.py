from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ecomapp.models import product, dairyProducts
from ecomapp.models.product import Product
from ecomapp.serializers.product_serializer import ProductSerializer
from ecomapp.serializers.product_serializer import DairyProductsSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


class ListCreateProductAPIView(APIView):
    def get(self,request):
        #products = Product.objects.all().filter(price__gt=30)
        products = Product.objects.raw("select * from ecomapp_product where price between 30 and 60")
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = request.data
        decoded_data = ProductSerializer(data=data)
        if not decoded_data.is_valid():
            return Response(decoded_data.errors, status=status.HTTP_400_BAD_REQUEST)
        decoded_data.save()
        return Response(decoded_data.data, status=status.HTTP_201_CREATED)


class DairyListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = DairyProductsSerializer


class DairyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = DairyProductsSerializer