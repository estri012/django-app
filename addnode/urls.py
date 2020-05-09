from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_node, name='add-node'),
]