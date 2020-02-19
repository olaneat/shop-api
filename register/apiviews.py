from .serializers import UserSerializer
from  register.models import CustomUser
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class =UserSerializer

class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    
