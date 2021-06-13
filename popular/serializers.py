from rest_framework import serializers
from .models import Popular

class PopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Popular
        fields = ('id', 'date','title', 'author','description' ,'link','imgsrc')