# from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from users.models import User
from users.serializers import UserListSerializer, UserDetailSerializer


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
