from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Category
from .serializer import CategorySerializer
from rest_framework import status 

# Create your views here.
@api_view(['GET', 'POST'])
def category_list(request):
 if request.method=="GET":
    category=Category.objects.all()
    serializer = CategorySerializer(category, many=True) #serialization: object is converted into json 
    return Response(serializer.data)
 elif request.method=='POST': #deserialization: json format data is converted to object 
     serializer = CategorySerializer(data= request.data)
     serializer.is_valid(raise_exception=True)
     serializer.save()
     #return Response({"datail": "New data created", "data": serializer.data}, status= 201) OR, 
     return Response({"datail": "New data created", "data": serializer.data}, status=status.HTTP_201_CREATED)
    

#To get the single data: 

@api_view(['GET', 'DELETE', 'PUT'])
def category_detail(request, id):
   category = Category.objects.get(id=id)
   if request.method=='GET':
      serializer = CategorySerializer(category)
      return Response(serializer.data)
   
   elif request.method=='PUT':
      serializer=CategorySerializer(category, data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({"datail":"data is changed", "data": serializer.data})
   
   elif request.method=='DELETE':
      category.delete()
      #return Response({"datail":"data has been deleted"}, status=204) Or, 
      return Response({"datail":"data has been deleted"}, status=status.HTTP_204_NO_CONTENT)  
   

