from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from.models import Category, OrderItems
from .serializer import CategorySerializer
from rest_framework import status 

#from rest_framework.views import APIView
from rest_framework import mixins 
#from rest_framework import generics
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

# Create your views here.


class CategoryAPIView(ListCreateAPIView):  #Using the combined form from generics 
#class CategoryAPIView( CreateAPIView, ListAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):  #Using the combined form form generics
#class CategoryDetailAPIView(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
   queryset = Category.objects.all()
   serializer_class = CategorySerializer
   #lookup_field = 'name'
   
   def delete(self, request, *args, **kwargs): #or destroy, both can be used
      category = self.get_object()   #it gets objects and filter using lookup fields from url <id> 
      items = OrderItems.objects.filter(food__category = category).count()
      if items>0:
         return Response({"datail":"Protected: Category cannot be deleted. Related to OrderItems. "})
      category.delete()
      return Response({"datail":"data has been deleted"}, status=status.HTTP_204_NO_CONTENT)  
   








# #GENERICS API: 
# class CategoryAPIView(generics.GenericAPIView):
#    queryset = Category.objects
#    serializer_class = CategorySerializer
   
#    def get(self, request):
#       category = self.queryset.all()
#       serializer = self.serializer_class(category, many=True)
#       return Response(serializer.data)
   





# #CLASS BASED API:-------------------------------------------------

# class CategoryList(APIView):

#  def get(self, request):
#     category=Category.objects.all()
#     serializer = CategorySerializer(category, many=True) #serialization: object is converted into json 
#     return Response(serializer.data)
 
#  def post(self, request): 
#      serializer = CategorySerializer(data= request.data)
#      serializer.is_valid(raise_exception=True)
#      serializer.save()
#      #return Response({"datail": "New data created", "data": serializer.data}, status= 201) OR, 
#      return Response({"datail": "New data created", "data": serializer.data}, status=status.HTTP_201_CREATED)
    

# #To get the single data: 

# class CategoryDetails(APIView):
#  def get(self, request, id):
#    category = Category.objects.get(id=id)
#    serializer = CategorySerializer(category)
#    return Response(serializer.data)
   
 
#  def put(self, request, id):
#    category = Category.objects.get(id=id)
#    serializer=CategorySerializer(category, data=request.data)
#    serializer.is_valid(raise_exception=True)
#    serializer.save()
#    return Response({"datail":"data is changed", "data": serializer.data})
   
#  def delete(self, request, id):
#    category = Category.objects.get(id=id)
#    items = OrderItems.objects.filter(food__category = category).count()
#    if items>0:
#       return Response({"datail":"cannot be deleted, protected error"})
#    category.delete()
#    return Response({"datail":"data has been deleted"}, status=status.HTTP_204_NO_CONTENT)  
   






# #FUNCTION BASED API: ---------------------------------------------

# @api_view(['GET', 'POST'])
# def category_list(request):
#  if request.method=="GET":
#     category=Category.objects.all()
#     serializer = CategorySerializer(category, many=True) #serialization: object is converted into json 
#     return Response(serializer.data)
 
#  elif request.method=='POST': #deserialization: json format data is converted to object 
#      serializer = CategorySerializer(data= request.data)
#      serializer.is_valid(raise_exception=True)
#      serializer.save()
#      #return Response({"datail": "New data created", "data": serializer.data}, status= 201) OR, 
#      return Response({"datail": "New data created", "data": serializer.data}, status=status.HTTP_201_CREATED)
    

# #To get the single data: 

# @api_view(['GET', 'DELETE', 'PUT'])
# def category_detail(request, id):
#    category = Category.objects.get(id=id)
#    if request.method=='GET':
#       serializer = CategorySerializer(category)
#       return Response(serializer.data)
   
#    elif request.method=='PUT':
#       serializer=CategorySerializer(category, data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({"datail":"data is changed", "data": serializer.data})
   
#    elif request.method=='DELETE':
#       category.delete()
#       #return Response({"datail":"data has been deleted"}, status=204) Or, 
#       return Response({"datail":"data has been deleted"}, status=status.HTTP_204_NO_CONTENT)  
   

