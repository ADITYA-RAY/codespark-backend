from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrendingSerializer
from .models import Trending

# Create your views here.

class TrendingView(viewsets.ModelViewSet):
    serializer_class = TrendingSerializer
    queryset = Trending.objects.all()

def index(request):
    return render(request,'index.html')
