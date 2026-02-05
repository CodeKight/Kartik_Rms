from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import response, serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.
class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None: 
            raise serializers.ValidationError({"deatail":"Both field are required"})
        
        #authenticating username and password with that stored in the database: 
        user = authenticate(username = username, password = password)  #same as, User.objects.filter(username= usernname, password = password)
        if user: 
            token,_=Token.objects.get_or_create(user = user)
            print(_) 
            return response.Response({"username": username, "token":token.key}, 201, "hello")    #Syntax of Response:  Resposnse(data="val", status="status_code")  , data & status are keywords. 
        return response.Response({"detail":"User doesn't exists."})
    
    
    
    
    
#Note: 

 #syntax of Response: 
 # Resposnse(data, status)
 # or 
 # Resposnse(data='val', status='stautus_code') 
 # or 
 # Resposnse("val", "status_code")  where data & status are the fixed keywords. 
            