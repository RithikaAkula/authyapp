from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    LoginSerializer, RegistrationSerializer
)
from .renderers import UserJSONRenderer
from rest_framework.views import exception_handler



class RegistrationAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)

    serializer_class = RegistrationSerializer

    def post(self, request):
        # user = request.data.get('user', {})

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # serializer.is_valid(raise_exception=True)
        # serializer.save()

        # return Response(serializer.data, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)

    serializer_class = LoginSerializer

    def post(self, request):
        # user = request.data.get('user', {})

        serializer = self.serializer_class(data=request.data)

        
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        # if serializer.errors.get('password'):
        #     return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
        # if serializer.errors.get('non_field_errors'):
        #     return Response(serializer.data,status=status.HTTP_401_UNAUTHORIZED)
        

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        # serializer.is_valid(raise_exception=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)

