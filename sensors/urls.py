from django.urls import path
from . import views
from restapi.models import Data, Node

urlpatterns = [
    path('accelero-x/', views.accelero_x, name='accelero-x'),
    path('accelero-y/', views.accelero_y, name='accelero-y'),
    path('accelero-z/', views.accelero_z, name='accelero-z'),
    path('gyro-x/', views.gyro_x, name='gyro-x'),
    path('gyro-y/', views.gyro_y, name='gyro-y'),
    path('gyro-z/', views.gyro_z, name='gyro-z'),
    path('moisture/', views.moisture, name='moisture'),
    path('vibration/', views.vibration, name='vibration'),
    path('displacement/', views.displacement, name='displacement'),
    path('angular/', views.angular, name='angular'),
]