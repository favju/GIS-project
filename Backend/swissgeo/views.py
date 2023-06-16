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

    # def get_length(self, pk=None):
    #     if self.queryset.exists():
    #         first_slope = self.queryset.get(pk=pk)
    #         first_slope.geom.transform(3857)
    #          # Accessing the length of the geom
    #         return first_slope.geom.length

    #     else:
    #         return None

    # def get_nearby_slopes(self, distance, pk=None):
    #     if self.queryset.exists():
    #         ref_slope = self.queryset.get(pk=pk)
    #         nearby_slopes_query = self.queryset.exclude(pk=pk)
    #         nearby_slopes = nearby_slopes_query.filter(
    #             geom__distance_lte=(ref_slope.geom, distance)
    #         ).values_list('id', flat=True)
    #         return nearby_slopes
    #     else:
    #         return None

    # def calculate_height(self, pk=None):
    #     try:
    #         slope = self.queryset.get(pk=pk)
    #         geom = slope.geom
    #         if geom:
    #             lineList = list(geom.coords)
    #             elevations = []
    #             for line_coords in lineList:
    #                 line = LineString(line_coords)
    #                 for point_coords in line.coords:
    #                     point = Point(point_coords)
    #                     # Replace 'elevation_field' with the actual field name for elevation in your model
    #                     elevation = self.queryset.filter(geom__contains=point).values_list('z', flat=True).first()
    #                     if elevation is not None:
    #                         elevations.append(elevation)

    #             if elevations:
    #                 return max(elevations), min(elevations)

    #         return None, None

    #     except Slope.DoesNotExist:
    #         return None, None

    # def retrieve(self, request, *args, **kwargs):
    #     slope_id= kwargs.get('pk')
    #     distance = 1
    #     length = self.get_length(pk=slope_id)
    #     nearby_slopes = self.get_nearby_slopes(distance, pk=slope_id)
    #     highest_height, lowest_height = self.calculate_height(pk=slope_id)

    #     response_data = {}
    #     if length is not None:
    #         response_data['length'] = length
    #     else:
    #         return JsonResponse({'message': 'Slope not found'}, status=404)

    #     if nearby_slopes is not None:
    #         response_data['nearby_slopes'] = list(nearby_slopes)
    #     else:
    #         response_data['nearby_slopes'] = []

    #     # if highest_height is not None and lowest_height is not None:
    #     #     response_data['highest_height'] = highest_height
    #     #     response_data['lowest_height'] = lowest_height


    #     return JsonResponse(response_data)