from rest_framework import serializers 
from .models import Category


# SERIALIZATION USING MODEL SERIALIZER:

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields='__all__'
        #fields=['id', 'name']
        #exclude=['name']
    
    # using save method to avoid duplicate data entry 
    def save(self, **kwargs):
        validated_data = self.validated_data
        category = Category.objects.filter(name = validated_data.get('name')).count()
        if category > 0:
          raise serializers.ValidationError({"datail":"This category already exists."})
        return super().save(**kwargs)
    
    # # overwriting the existing create and update to prevent duplicate data entry 
    
    # def create(self, validated_data):
    #    category = Category.objects.filter(name = validated_data.get('name')).count()
    #    if category > 0:
    #       raise serializers.ValidationError({"datail":"This category already exists."})
    #    #category.save()
    #    return super().create(validated_data)
   
    # def update(self, instance, validated_data):
    #    category = Category.objects.filter(name = validated_data.get('name')).count()
    #    if category > 0:
    #      raise serializers.ValidationError({"datail":"This category already exists."})
    #    #category.save()
    #    return super().update(instance, validated_data)
        
    






# # NORMAL SERIALIZATION: 

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
 
 
     
 