from django.contrib import admin
from django.contrib.gis import admin

from .models import Skilift

# Register your models here.
admin.site.register(Skilift, admin.OSMGeoAdmin)

