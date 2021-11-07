from django.http import response
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from core.serializers import UserRegisteration

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
