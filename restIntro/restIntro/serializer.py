from rest_framework import serializers

from rest_framework import serializers
from restIntro.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"