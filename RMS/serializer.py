from rest_framework import serializers 
from .models import Category


# SERIALIZATION USING MODEL SERIALIZER:

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
        #fields=['id', 'name']
        #exclude=['name']
        
    






#NORMAL SERIALIZATION 

# class CategorySerializer(serializers.Serializer):
#  name = serializers.CharField(max_length=20)
#  id = serializers.IntegerField(read_only=True)
#  #validated_data = {"name": "api form", "age": 23}
 
#  def create(self, validated_data):
#      category = Category.objects.create(name = validated_data.get('name') ) #, age=validated_data.get('age') , to also display age 
#      #Or, Category.objects.create(**validated_data) #Taking all data form the qwargs 
#      return category
 
#  #to update
#  def update(self, instance, validated_data):
#      instance.name=validated_data.get('name', instance.name)
#      return instance
 
 
     
 