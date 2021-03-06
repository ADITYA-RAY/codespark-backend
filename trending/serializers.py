from rest_framework import serializers
from .models import Trending

class TrendingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trending
        fields = ('id', 'date','title', 'author','description' ,'link','imgsrc')