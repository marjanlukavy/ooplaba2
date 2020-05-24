from rest_framework import serializers
from .models import Dog

class DogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = ['id','name','weight','owner','email','website','published_date']
