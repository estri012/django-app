from django.urls import path
from . import views
from restapi import views
from restapi.models import Data, Node
from sensors.views import SoilMoisture, Vibration, Displacement, AcceleroX, AcceleroY, AcceleroZ, GyroX, GyroY, GyroZ

urlpatterns = [
    path('soil-moisture/', SoilMoisture.as_view(), name='soilmoisture'),
    path('vibration/', Vibration.as_view(), name="vibration"),
    path('displacement/', Displacement.as_view(), name="displacement"),
    path('accelero-x/', AcceleroX.as_view(), name="accelero-x"),
    path('accelero-y/', AcceleroY.as_view(), name="accelero-y"),
    path('accelero-z/', AcceleroZ.as_view(), name="accelero-z"),
    path('gyro-x/', GyroX.as_view(), name="gyro-x"),
    path('gyro-y/', GyroY.as_view(), name="gyro-y"),
    path('gyro-z/', GyroZ.as_view(), name="gyro-z"),
]