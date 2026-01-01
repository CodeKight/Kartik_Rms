from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Category(models.Model):  
    name=models.CharField(max_length=100)
    
class Food(models.Model):   
    name=models.CharField(max_length=100)
    description= models.TextField()
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True) # CASCADE, SET_NULL, PROTECT
    
class Table(models.Model):
    number=models.CharField(max_length=100)  #'8', 'A'
    capacity=models.IntegerField()
    available=models.BooleanField(default=False)
    
class Order(models.Model):
    PENDING='P'
    COMPLETE='C'
    DELIVERED='D'
    STATUS_CHOICE=[
        (PENDING, "Pending"),
        (COMPLETE, "Pomplete"),
        (DELIVERED, "Delivered")
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    table=models.ForeignKey(Table, on_delete=models.CASCADE, null=True, blank=True)
    total_price=models.FloatField()
    status=models.CharField(max_length=1, choices=STATUS_CHOICE, default=PENDING)
    payment_status=models.BooleanField(default=False)
    
    
class OrderItems(models.Model):
    order=models.ForeignKey(Order, on_delete=models.PROTECT)
    food=models.ForeignKey(Food, on_delete=models.PROTECT)
    
    
    
    