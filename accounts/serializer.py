from django.contrib.auth import get_user_model
from rest_framework import serializers
User=get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password','confirm_password']
        extra_kwarg={'password':{'write_only':True}}
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return attrs
    def create(self, validated_data):
        validated_data.pop('confirm_password') 
        user = User.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','password']
    