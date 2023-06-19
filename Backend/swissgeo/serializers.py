from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Skilift, Slope, Restaurant
from django.core.serializers import serialize
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometryField
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class SkiliftGeoSerializer(GeoFeatureModelSerializer):    
    class Meta:
        model = Skilift
        fields = '__all__'
        geo_field = 'geom'

class SkiliftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skilift
        fields = ['id', 'name', 'open']

class SlopeGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Slope
        fields = '__all__'
        geo_field = 'geom'

class RestaurantGeoSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
        geo_field = 'geom'

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'open']