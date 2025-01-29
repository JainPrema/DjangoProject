from rest_framework import generics, status
from rest_framework.views import APIView

from restIntro.models import User
from restIntro.serializer import UserSerializer
from restIntro.views import users
from .models import User
from .serializer import UserSerializer
from rest_framework.response import Response

class UserListCreateAPIView(APIView):
    def get(self,request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True)
        return Response(serialized.data)

    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        return Response(serialized.errors)
