from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display=['id', 'name']
  
  
admin.site.register(Food)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(OrderItems)

