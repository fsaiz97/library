from rest_framework import serializers
from resources.models import *

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
        
class characterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'

class placeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class locationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'



class loanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
