import re
from rest_framework import serializers
from authorization.models import User
from django.contrib.auth import authenticate


class SignUpAPISerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(
        max_length=50,
        min_length=8,
        write_only=True
    )
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
        
    def create(self, validated_data):
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', validated_data['password']):
            raise serializers.ValidationError({'password': 'Bad password format'})
        # manager method
        return User.objects.create_user(**validated_data)
        
        
        
        
class SignInAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'token']
        #read_only_fields = ['token']
        write_only_fields = ['password']

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    

    def validate(self, data):
        dictErrors = {}
        if not re.fullmatch(r'[a-zA-Z0-9\.\-\_]{4,100}[@][a-z]{2,6}\.[a-z]{2,6}\.?[a-z]{2,6}?', data['email']):
            dictErrors['email'] = 'Bad email format'
        if not re.fullmatch(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}', data['password']):
            dictErrors['password'] = 'Bad password format'

        if len(dictErrors) > 0:
            raise serializers.ValidationError(dictErrors)
        
        user = authenticate(username=data['email'], password=data['password'])
        if user is None:
            raise serializers.ValidationError('The user with such email is not registered or incorrect password')
        
        return {'email': data['email'],
                'token': user.token
                }
        
        
        #return data