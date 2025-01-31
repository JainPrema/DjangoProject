from rest_framework.serializers import ModelSerializer

from ecom.models import User, ShippingAddress

class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class ShippingAddressSerializer(ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = "__all__"