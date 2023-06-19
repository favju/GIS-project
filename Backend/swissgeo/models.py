from django.contrib.gis.db import models
from django.contrib.gis.db.models import Union

# Create your models here.from django.contrib.gis.db import models


class Skilift(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=10, decimal_places=4)
    maxseat = models.PositiveIntegerField()
    type = models.CharField(max_length=200)
    open = models.BooleanField()
    image = models.CharField(max_length=200)
    geom = models.MultiLineStringField()

    class Meta:
        db_table = "skilifts"

    def __str__(self):
        return self.name


class Slope(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=10, decimal_places=4)
    geom = models.MultiLineStringField()

    class Meta:
        db_table = "slopes"

    def __str__(self):
        return self.name
    
class Restaurant(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    height = models.IntegerField()
    open = models.BooleanField()
    image = models.CharField(max_length=250)
    geom = models.MultiPolygonField()
    
    class Meta:
        db_table = "restaurants"

    def __str__(self):
        return self.name
        
