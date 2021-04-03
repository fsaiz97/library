from rest_framework import serializers
from resources.models import *
from django.utils import timezone

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

class authorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class resourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'

class loanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class loanReadableSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source='get_status_display')
    account_name = serializers.CharField(source='account.user.username')
    resource_title = serializers.CharField(source='resource.title')

    class Meta:
        model = Loan
        fields = ['id', 'check_out_date', 'return_date', 'status', 'account_name', 'resource_title']