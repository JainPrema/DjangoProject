from rest_framework import serializers
from ecomapp.models import Product, dairyProducts

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DairyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = dairyProducts
        fields = '__all__'
