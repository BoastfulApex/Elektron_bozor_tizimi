from rest_framework import serializers
from django.contrib.auth.validators import UnicodeUsernameValidator
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password']
        extra_kwargs = {
            'username':{
                'validators':[UnicodeUsernameValidator()]
            }
        }


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Employee
        fields = '__all__'
