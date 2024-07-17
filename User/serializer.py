from rest_framework import serializers
from .models import authCredentials
from .models import createUser
from .models import userAccount

class authSerializer(serializers.ModelSerializer):
    class Meta:
        model = authCredentials
        fields = ["id","emailid","password","timestamp"]

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = createUser
        fields = ["id","name","mobile","address","account_number","timestamp"]

class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = userAccount
        fields = ["id","account_number","transaction","type","timestamp"]