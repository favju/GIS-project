from .models import Skilift, Slope, Restaurant
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, SkiliftGeoSerializer, SlopeGeoSerializer, RestaurantGeoSerializer, RestaurantSerializer, SkiliftSerializer
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
    serializer_class = SkiliftGeoSerializer
    permission_classes = [permissions.AllowAny]

class SkiliftOpenViewSet(viewsets.ModelViewSet):
    queryset = Skilift.objects.all()
    serializer_class = SkiliftSerializer
    permission_classes = [permissions.AllowAny]
        
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantGeoSerializer
    permission_classes = [permissions.AllowAny]

class RestaurantOpenViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.AllowAny]

class SlopeViewSet(viewsets.ModelViewSet):
    queryset = Slope.objects.all()
    serializer_class = SlopeGeoSerializer
    permission_classes = [permissions.AllowAny]

class UnionSlopeViewSet(viewsets.ModelViewSet):
    queryset = Slope.objects.all()
    serializer_class = SlopeGeoSerializer
    permission_classes = [permissions.AllowAny]

    def get_names(self):
        names = Slope.objects.order_by(Lower('name')).values_list('name', flat=True).distinct()
        return names
    
    def get_difficulties_by_names(self, name):
        difficulties = Slope.objects.filter(name=name).order_by(Lower('difficulty')).values_list('difficulty', flat=True).distinct()
        return difficulties
    
    def union_Slope(self, name, difficulty, id):

        slopes = Slope.objects.exclude(name='Connector')

        if name:
            slopes = slopes.filter(name__contains=name)
        if difficulty:
            slopes = slopes.filter(difficulty__contains=difficulty)

        if slopes.exists():
            fusedSlop = slopes[0].geom
            total_length = 0
            for query in slopes:
                fusedSlop = fusedSlop.union(query.geom)
                total_length += query.length 
            fused_slope = Slope(id=id, name=name, difficulty=difficulty, length=total_length, geom=fusedSlop)
            return fused_slope
    
    def union_all_Slopes(self):
        names = self.get_names()
        id = 100
        slopes = []

        for name in names:
            difficulties = self.get_difficulties_by_names(name)
            for difficulty in difficulties:
                fused_slope = self.union_Slope(name, difficulty, id)
                if fused_slope:
                    slopes.append(fused_slope)
                    id += 1

        return slopes

    def list(self, request, *args, **kwargs):
        fused_slopes = self.union_all_Slopes()

        serializer = self.get_serializer(fused_slopes, many=True)

        # Serialize as GeoJSON
        geojson = JSONRenderer().render(serializer.data)
        return HttpResponse(geojson, content_type='application/json')

        


