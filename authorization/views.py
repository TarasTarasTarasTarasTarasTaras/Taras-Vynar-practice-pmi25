#from rest_framework.views import APIView
from django.core import paginator
from rest_framework.generics import ListAPIView

from rest_framework.response import Response
from rest_framework import serializers, status, filters, permissions
from .models import User
from .serializer import SignUpAPISerializer, SignInAPISerializer

from drf_yasg.utils import swagger_auto_schema

from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny



# Create your views here.



class SignUpAPI(ListAPIView):
    serializer_class = SignUpAPISerializer
    permission_classes = (AllowAny,)

    #@swagger_auto_schema()
    def post(self, request):
        serializerUser = self.serializer_class(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        serializerUser.save()
        
        return Response(serializerUser.data, status=status.HTTP_201_CREATED)
        
        
        
class SignInAPI(ListAPIView):
    serializer_class = SignInAPISerializer
    permission_classes = (AllowAny,)

    #@swagger_auto_schema()
    def post(self, request):
        serializerUser = self.serializer_class(data=request.data)
        serializerUser.is_valid(raise_exception=True)
        
        return Response(serializerUser.data, status=status.HTTP_200_OK)
        
        