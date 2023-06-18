from django.contrib import admin
from django.contrib.gis import admin

from .models import Skilift, Restaurant, Slope

# Register your models here.
admin.site.register(Skilift, admin.OSMGeoAdmin)
admin.site.register(Slope, admin.OSMGeoAdmin)
admin.site.register(Restaurant, admin.OSMGeoAdmin)

