from .models import Skilift, Slope, Restaurant
from django.contrib.auth.models import User
from django.core.serializers import serialize
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, SkiliftSerializer, SlopeSerializer, RestaurantSerializer
from django.http import JsonResponse
from django.contrib.gis.db.models import Union
from django.contrib.gis.geos import Point
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer

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
        
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permissions_classes = [permissions.AllowAny]
    
class SlopeViewSet(viewsets.ModelViewSet):
    queryset = Skilift.objects.all()
    serializer_class = SlopeSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request, *args, **kwargs):
        name = request.GET.get('name')
        difficulty = request.GET.get('difficulty')

        queryset = Slope.objects.all()
        if name:
            queryset = queryset.filter(name__contains=name)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        fusedSlop = queryset[0].geom
        for query in queryset:
            fusedSlop = fusedSlop.union(query.geom)

        fused_slope = Slope(id=9999, name=name, difficulty=difficulty, length=fusedSlop.length, geom=fusedSlop )

        serializer = self.get_serializer([fused_slope], many=True)

        # Serialize as GeoJSON
        geojson = JSONRenderer().render(serializer.data)
        return HttpResponse(geojson, content_type='application/json')

        


