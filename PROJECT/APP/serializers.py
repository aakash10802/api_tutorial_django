from rest_framework import serializers
from .models import Person 

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','age','place']

