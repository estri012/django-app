from django.urls import path
from . import views
from restapi import views
from restapi.models import Data, Node
from sensors.views import SoilMoisture

urlpatterns = [
    path('soil-moisture/', SoilMoisture.as_view(), name='soilmoisture'),
]