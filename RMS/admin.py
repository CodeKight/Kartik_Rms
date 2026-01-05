from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'name']

  
@admin.register(Food)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'name','description', 'price', 'category']
  list_filter=['category']
  search_fields=['name']
  
  
# class OrderItemInline(admin.StackedInline):
class OrderItemInline(admin.TabularInline):
   model = OrderItems
   autocomplete_fields = ['food']



@admin.register(Table)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'number', 'capacity', 'available']


@admin.register(Order)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'user', 'table', 'total_price', 'status', 'payment_status']
  list_filter=['status', 'payment_status']
  search_fields=['user__username' ]
  inlines = [OrderItemInline]
  
  
  
@admin.register(OrderItems)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'order', 'food']
 


  
  
# admin.site.register(Food)
# admin.site.register(Table)
# admin.site.register(Order)
# admin.site.register(OrderItems)

