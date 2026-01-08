from rest_framework import serializers 
from .models import Category





class CategorySerializer(serializers.ModelSerializer):
   class Meta:
      model = Category
      fields = '__all__'
      # fields = ['id','name']
      # exclude = ['name']


# class CategorySerializer(serializers.Serializer):
#    id = serializers.IntegerField(read_only=True)
#    name = serializers.CharField()

#    def create(self, validated_data):
#       category = Category.objects.create(name = validated_data.get('name'))
#       # Category.objects.create(**validated_data)
#       return category

#    def update(self, instance, validated_data):        # validated_data = {"name":"drinks"}
#       instance.name = validated_data.get('name', instance.name)
#       instance.save()
#       return instance



# instance = Todo.objects.get(id = 1)
# instance.title # print the title of id 1



#-----------------------------------------------------------
# class CategorySerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=20)
#     id = serializers.IntegerField(read_only=True)
#  #validated_data = {"name": "api form", "age": 23}
#     def create(self, validated_data):
#         category = Category.objects.create(name = validated_data.get('name') ) #, age=validated_data.get('age') , to also display age 
#       #Or, Category.objects.create(**validated_data) #Taking all data form the qwargs 
#         return category
 
#     def update(self, instance, validated_data):
#         instance.name(validated_data.get('name', instance.name))
#         instance.save()
#         return instance
    
 