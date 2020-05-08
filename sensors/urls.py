from django.urls import path
from . import views
from restapi import views
from restapi.models import Data, Node
from sensors.views import SensorNode1

urlpatterns = [
    path('node1/', SensorNode1.as_view(), name='node1'),
]