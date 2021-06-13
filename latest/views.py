from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LatestSerializer
from .models import Latest

# Create your views here.

class LatestView(viewsets.ModelViewSet):
    serializer_class = LatestSerializer
    queryset = Latest.objects.all()

def index(request):
    return render(request,'index.html')
