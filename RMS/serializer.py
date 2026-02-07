from rest_framework import serializers 
from .models import Category, Food, Order, OrderItems


#Food Serializer: 

class FoodSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()
    #category = serializers.StringRelatedField()
    class Meta: 
        model = Food 
        fields = ['id', 'name', 'description', 'price', 'price_with_tax', 'category']
        
    def get_price_with_tax(self, food:Food):
        return food.price*0.13 + food.price

#orderitem serializer: 

class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = OrderItems
        fields = '__all__'

#order serializer:
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default = serializers.CurrentUserDefault())
    items = OrderItemsSerializer
    class Meta:
        model = Order 
        fields = ["user", "table", "total_price", "status", "payment_status", "items"]

















# SERIALIZATION USING MODEL SERIALIZER:----------------------------------
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
        
    






# # NORMAL SERIALIZATION: -----------------------------------------

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
 
 
     
 