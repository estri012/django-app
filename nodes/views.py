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
class NodeList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'nodelist.html')

class AddNode(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'addnode.html')

def nodesensors(request, node_node_id):
    try:
        node = Node.objects.get(pk=node_node_id)
    except Node.DoesNotExist:
        raise Http404("Node does not exist")
    return render(request, 'nodesensors.html', {'node': node})
