from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from rest_framework.views import APIView
from restapi.serializers import DataSerializer, NodeSerializer
from restapi.models import Data, Node
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.views.generic import View
from django.http import Http404
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from restapi.serializers import DataSerializer, NodeSerializer
from restapi.models import Data, Node
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from rest_framework.views import APIView
from django.shortcuts import redirect
# Create your views here.
def accelero_x(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_x.html', context)

def accelero_y(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_y.html', context)

def accelero_z(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'accelero_z.html', context)

def gyro_x(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_x.html', context)

def gyro_y(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_y.html', context)

def gyro_z(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'gyro_z.html', context)

def moisture(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'moisture.html', context)

def vibration(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'vibration.html', context)

def displacement(request):
    sensor_list = Node.objects.order_by('node_id')
    context = {'sensor_list': sensor_list}
    return render(request, 'displacement.html', context)

