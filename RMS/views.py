from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Category
from .serializer import CategorySerializer

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
     return Response({"datail": "New data created", "data": serializer.data})
    