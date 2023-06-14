from django.db import models
from django.contrib.gis.db import models

# Create your models here.from django.contrib.gis.db import models


class Skilift(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=10, decimal_places=4)
    maxseat = models.PositiveIntegerField()
    type = models.CharField(max_length=200)
    geom = models.MultiLineStringField(srid=4326, null=True)

    class Meta:
        db_table = "skilifts"

    def __str__(self):
        return self.name


class Slope(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=200)
    length = models.DecimalField(max_digits=10, decimal_places=4)
    geom = models.MultiLineStringField(srid=4326, null=True)

    class Meta:
        db_table = "slopes"

    def __str__(self):
        return self.name
