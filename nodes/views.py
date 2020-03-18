from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def node1(request):
    return render(request, 'node1.html')