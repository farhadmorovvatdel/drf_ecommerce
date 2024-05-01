from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework import generics
from django.contrib.auth import authenticate
from .serializer import UserSerializer,UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
User=get_user_model()





class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request:Request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        refresh_token = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }, status=status.HTTP_201_CREATED)
      
class UserLoginAPIView(generics.CreateAPIView):
    serializer_class = UserLoginSerializer

    def create(self, request:Request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
        refresh_token = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh_token),
            'access': str(refresh_token.access_token),
        }, status=status.HTTP_201_CREATED)
      
