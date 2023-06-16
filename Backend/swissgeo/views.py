from .models import Skilift, Slope
from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, SkiliftSerializer, SlopeSerializer
from django.http import JsonResponse

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class SkiliftViewSet(viewsets.ModelViewSet):
    queryset = Skilift.objects.all()
    serializer_class = SkiliftSerializer
    permission_classes = [permissions.AllowAny]

class SlopeViewSet(viewsets.ModelViewSet):
    queryset = Slope.objects.all()
    serializer_class = SlopeSerializer
    permission_classes = [permissions.AllowAny]
