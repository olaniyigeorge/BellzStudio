from django.shortcuts import render
from rest_framework.viewsets import generics
from rest_framework import permissions

from .models import User, Profile
from .serializers import UserSerializer, ProfilesSerializer
import main.custom_permissions as cp 

# Create your views here.



class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.request.method == "GET":
            print(self.request.method)
            return [permissions.IsAdminUser(),]
        return super().get_permissions()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializer
    permission_classes = [permissions.IsAuthenticated, cp.IsOwnerOrReadOnly]
    

class ProfilesView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = "pk"