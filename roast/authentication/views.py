from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from authentication.serializers import UserLoginSerializer,UserRegisteration
from rest_framework.generics import CreateAPIView

# Create your views here.

class RegistrationView(CreateAPIView):
    serializer_class = UserRegisteration
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        staus_code = status.HTTP_201_CREATED
        response = {
            'success' : True,
            'status_code' : staus_code,
            'message' : 'Registered Successfully'
        }

        return Response(response, status=staus_code)

class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)