from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from restapi.serializers import DataSerializer, NodeSerializer
from restapi.models import Data, Node
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
import json
# Create your views here.
class SoilMoisture(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'soilmoisture.html')

class Vibration(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'vibration.html')

class Displacement(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'displacement.html')

class AcceleroX(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accelero-x.html')

class AcceleroY(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accelero-y.html')

class AcceleroZ(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accelero-z.html')

class GyroX(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gyro-x.html')

class GyroY(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gyro-y.html')

class GyroZ(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'gyro-z.html')