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
