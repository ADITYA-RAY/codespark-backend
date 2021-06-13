from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PopularSerializer
from .models import Popular

# Create your views here.

class PopularView(viewsets.ModelViewSet):
    serializer_class = PopularSerializer
    queryset = Popular.objects.all()

def index(request):
    return render(request,'index.html')
