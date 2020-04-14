from django.urls import path
from . import views
from restapi import views
from restapi.models import Data, Node
from nodes.views import Map

urlpatterns = [
    path('node-1/', Map.as_view(), name='node1'),
]