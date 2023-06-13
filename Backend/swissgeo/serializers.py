from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Skilift
from django.core.serializers import serialize
from rest_framework_gis.serializers import GeoFeatureModelSerializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name']

class SkiliftSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Skilift
        fields = '__all__'
        geo_field = 'geom'