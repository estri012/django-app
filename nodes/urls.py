from django.urls import path
from . import views

urlpatterns = [
    path('node-1/', views.node1, name='node1'),
]