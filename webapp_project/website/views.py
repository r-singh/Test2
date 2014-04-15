from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from website.serializers import UserSerializer, GroupSerializer
from .models import Genre
from .models import Tag
from .models import Book
from .models import Asset
from .models import Author


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows books to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = GroupSerializer
