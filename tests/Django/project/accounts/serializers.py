from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class EmpLeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmpLeaveRequest
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=64, min_length=8, write_only=True)
    # email = serializers.EmailField(max_length=64,min_length=4)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def validate(self, attrs):
        email = attrs.get('email', '')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('Email is already in use')})
        return super().validate(attrs)
    def create(self, validated_data):
        # password = validated_data.pop('password', None)
        # instance = self.Meta.model(**validated_data)
        # if password is not None:
        #     instance.set_password(password)
        # instance.save()
        # return instance
        return User.objects.create_user(**validated_data)