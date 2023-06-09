from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Canton
from django.template import loader
from django.http import Http404
from django.core.serializers import serialize

