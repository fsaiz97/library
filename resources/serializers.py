from rest_framework import serializers
from resources.models import Resource, Location, Subject


class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
