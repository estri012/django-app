from django.urls import path
from . import views
from restapi import views
from restapi.models import Data, Node
from nodes.views import NodeList, AddNode

urlpatterns = [
    path('nodelist/', NodeList.as_view(), name='nodelist'),
    path('addnode/', AddNode.as_view(), name='addnode'),
    path('chart/<int:node_node_id>/', views.nodesensors, name='nodesensors'),
]