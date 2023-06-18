from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Skilift, Slope, Restaurant
from django.core.serializers import serialize
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometryField
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class SkiliftSerializer(GeoFeatureModelSerializer):
    geom = GeometryField(source='transformed_geom')
    
    class Meta:
        model = Skilift
        fields = '__all__'
        geo_field = 'geom'

class SlopeSerializer(GeoFeatureModelSerializer):
    geom = GeometryField(source='transformed_geom')
    
    class Meta:
        model = Slope
        fields = '__all__'
        geo_field = 'geom'

class RestaurantSerializer(GeoFeatureModelSerializer):
    geom = GeometryField(source='transformed_geom')

    class Meta:
        model = Restaurant
        fields = '__all__'
        geo_field = 'geom'