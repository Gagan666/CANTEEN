from django.contrib.auth.hashers import make_password
from django.http import HttpResponse, QueryDict
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import NewUser
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return HttpResponse("hello")

class CreateUser(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(request.data)
        data = request.data
        #convert Querydict to python dictionary
        myDict = data.dict()
        try:
            user = NewUser.objects.get(phone=myDict['phone'])
            return Response({"message": "Phone number already present"})
        except ObjectDoesNotExist:
            user = NewUser.objects.create_user(user_name=myDict['user_name'], password=myDict['password'],phone=myDict['phone'])
            return Response({"message":"Successfully created"})




