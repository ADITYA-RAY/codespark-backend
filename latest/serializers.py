from rest_framework import serializers
from .models import Latest

class LatestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Latest
        fields = ('id', 'date','title', 'author','description' ,'link','imgsrc')