from rest_framework import serializers
from resources.models import Resource


class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'
